extern alias ProZip;
using System;
using System.IO;
using System.IO.Compression;
using System.Text;
using System.Text.Json;
using SafeZip = ProZip::Ionic.Zip.ZipFile;

var lab = Path.GetFullPath(Path.Combine(Environment.CurrentDirectory, "lab"));
if (Directory.Exists(lab)) throw new InvalidOperationException("Preserve prior lab");
Directory.CreateDirectory(lab);
var rows = new System.Collections.Generic.List<object>();
void Check(string id, bool value) => rows.Add(new { id, status = value ? "PASS" : "FAIL" });
string UnderLab(string relative)
{
    var path = Path.GetFullPath(Path.Combine(lab, relative));
    if (!path.StartsWith(lab + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase))
        throw new InvalidOperationException("Outside owned lab");
    return path;
}
bool nativeEscaped = false;
foreach (var variant in new[] { "native-overwrite", "native-no-overwrite", "bcl-overwrite" })
{
    var variantRoot = UnderLab(variant);
    var extract = UnderLab(Path.Combine(variant, "extract"));
    var canary = UnderLab(Path.Combine(variant, "sibling-canary.txt"));
    Directory.CreateDirectory(extract);
    var archive = UnderLab(Path.Combine(variant, "fixture.zip"));
    using (var zip = ZipFile.Open(archive, ZipArchiveMode.Create))
    using (var writer = new StreamWriter(zip.CreateEntry("../sibling-canary.txt").Open()))
        writer.Write("OWN_SYNTHETIC_CANARY_NO_SECRET");
    bool result;
    if (variant == "bcl-overwrite")
    {
        try { ZipFile.ExtractToDirectory(archive, extract, overwriteFiles: true); result = true; }
        catch (IOException) { result = false; }
    }
    else result = QuantConnect.Compression.Unzip(archive, extract, variant == "native-overwrite");
    var escaped = File.Exists(canary);
    if (variant == "native-overwrite")
    {
        nativeEscaped = escaped;
        Check("OBSERVE_NATIVE_OVERWRITE_BOUNDARY", result && escaped);
    }
    else Check("REJECT_TRAVERSAL_" + variant, !result && !escaped);
}
using (var encoded = new MemoryStream())
{
    using (var zip = new SafeZip()) { zip.AddEntry("fixture.txt", "OWN_SYNTHETIC_TEXT"); zip.Save(encoded); }
    encoded.Position = 0;
    using var zipRead = SafeZip.Read(encoded);
    using var decoded = new MemoryStream();
    zipRead["fixture.txt"].Extract(decoded);
    Check("FORK_IONIC_API_MEMORY_ROUNDTRIP", Encoding.UTF8.GetString(decoded.ToArray()) == "OWN_SYNTHETIC_TEXT");
    Check("FORK_ASSEMBLY_IS_DISTINCT", typeof(SafeZip).Assembly.GetName().Name == "ProDotNetZip");
}
Check("CANARY_REMAINS_INSIDE_OWNED_LAB", File.Exists(UnderLab("native-overwrite/sibling-canary.txt")));
Console.WriteLine("QL4_RESULT=" + JsonSerializer.Serialize(new {
    rows, native_unzip_overwrite_safety = nativeEscaped ? "FAIL_BOUNDARY_DEMONSTRATED" : "NOT_DEMONSTRATED",
    fork_full_lean_compatibility_accepted = false, no_production_patch_applied = true
}));
