using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Text;
using System.Text.Json;

var rows=new System.Collections.Generic.List<object>();
void Check(string id,bool result)=>rows.Add(new{id,status=result?"PASS":"FAIL"});
var host=Assembly.Load("LeanRemediationHostProbe");
Check("NATIVE_MAIN_COMPILED_NOT_INVOKED",host.EntryPoint?.DeclaringType?.FullName=="QuantConnect.Lean.Launcher.Program");
Check("ENGINE_TYPE_LOAD",Assembly.Load("QuantConnect.Lean.Engine").GetType("QuantConnect.Lean.Engine.Engine",true)!=null);
var lab=Path.GetFullPath(Path.Combine(Environment.CurrentDirectory,"lab"));
if(Directory.Exists(lab))throw new InvalidOperationException("Preserve lab");
Directory.CreateDirectory(lab);
foreach(var mode in new[]{"traversal","safe"})
{
    var dir=Path.GetFullPath(Path.Combine(lab,mode,"extract"));
    var canary=Path.GetFullPath(Path.Combine(lab,mode,"sibling-canary.txt"));
    if(!dir.StartsWith(lab+Path.DirectorySeparatorChar)||!canary.StartsWith(lab+Path.DirectorySeparatorChar))throw new InvalidOperationException("Outside lab");
    Directory.CreateDirectory(dir);var file=Path.Combine(lab,mode,"fixture.zip");
    using(var archive=ZipFile.Open(file,ZipArchiveMode.Create))
    using(var writer=new StreamWriter(archive.CreateEntry(mode=="traversal"?"../sibling-canary.txt":"safe.txt").Open()))writer.Write("OWN_SYNTHETIC_FIXTURE");
    var ok=QuantConnect.Compression.Unzip(file,dir,true);
    if(mode=="traversal")Check("PATCHED_HELPER_DENIES_TRAVERSAL",!ok&&!File.Exists(canary));
    else Check("PATCHED_HELPER_SAFE_FILE",ok&&File.ReadAllText(Path.Combine(dir,"safe.txt"))=="OWN_SYNTHETIC_FIXTURE");
}
using(var encoded=new MemoryStream())
{
    using(var zip=new Ionic.Zip.ZipFile()){zip.AddEntry("f.txt","OWN_TEXT");zip.Save(encoded);}
    encoded.Position=0;using var reader=Ionic.Zip.ZipFile.Read(encoded);using var decoded=new MemoryStream();reader["f.txt"].Extract(decoded);
    Check("FORK_API_ROUNDTRIP_WITH_REBUILT_GRAPH",Encoding.UTF8.GetString(decoded.ToArray())=="OWN_TEXT");
    Check("FORK_DISTINCT_ASSEMBLY",typeof(Ionic.Zip.ZipFile).Assembly.GetName().Name=="ProDotNetZip");
}
Console.WriteLine("QL5_RESULT="+JsonSerializer.Serialize(new{rows,engine_run=false,production_pin_accepted=false}));
