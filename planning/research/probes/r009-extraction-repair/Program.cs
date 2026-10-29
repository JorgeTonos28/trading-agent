using System;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Text.Json;
var lab=Path.GetFullPath(Path.Combine(Environment.CurrentDirectory,"lab"));
if(Directory.Exists(lab))throw new InvalidOperationException("Preserve lab");Directory.CreateDirectory(lab);
var rows=new System.Collections.Generic.List<object>();
void Check(string id,bool ok)=>rows.Add(new{id,status=ok?"PASS":"FAIL"});
byte[] Zip(string entry,string text){using var b=new MemoryStream();using(var z=new ZipArchive(b,ZipArchiveMode.Create,true))using(var w=new StreamWriter(z.CreateEntry(entry).Open()))w.Write(text);return b.ToArray();}
foreach(var route in new[]{"unzip","bytes","file"})
{
 var place=Path.Combine(lab,route);Directory.CreateDirectory(place);
 var extract=Path.Combine(place,"extract");Directory.CreateDirectory(extract);
 var fixture=Path.Combine(place,"fixture.zip");File.WriteAllBytes(fixture,Zip("../sibling-canary.txt","OWN_CANARY"));
 bool rejected=false;
 try{if(route=="unzip")rejected=!QuantConnect.Compression.Unzip(fixture,extract,true);
 else if(route=="bytes")QuantConnect.Compression.UnzipToFolder(File.ReadAllBytes(fixture),extract);
 else {var own=Path.Combine(extract,"fixture.zip");File.Copy(fixture,own);QuantConnect.Compression.UnzipToFolder(own);}}
 catch(IOException){rejected=true;}
 Check("REPAIR_REJECTS_TRAVERSAL_"+route,rejected&&!File.Exists(Path.Combine(place,"sibling-canary.txt")));
}
var safe=Path.Combine(lab,"safe");Directory.CreateDirectory(safe);
var paths=QuantConnect.Compression.UnzipToFolder(Zip("nested/f.txt","FIRST"),safe);
Check("NESTED_CONTENT",File.ReadAllText(Path.Combine(safe,"nested/f.txt"))=="FIRST");
Check("RETURNED_ABSOLUTE_FILE_PATH",paths.Count==1&&Path.GetFullPath(paths[0])==Path.Combine(safe,"nested/f.txt"));
QuantConnect.Compression.UnzipToFolder(Zip("nested/f.txt","SECOND"),safe);
Check("BYTE_OVERWRITE_PRESERVED",File.ReadAllText(Path.Combine(safe,"nested/f.txt"))=="SECOND");
var archive=Path.Combine(lab,"safe.zip");File.WriteAllBytes(archive,Zip("f.txt","FILE"));
var filePaths=QuantConnect.Compression.UnzipToFolder(archive);
Check("FILE_OVERLOAD_CONTENT_AND_LIST",File.ReadAllText(Path.Combine(lab,"f.txt"))=="FILE"&&filePaths.Count==1);
var outDir=Path.Combine(lab,"normal-unzip");Directory.CreateDirectory(outDir);
Check("UNZIP_SAFE",QuantConnect.Compression.Unzip(archive,outDir,true)&&File.ReadAllText(Path.Combine(outDir,"f.txt"))=="FILE");
File.WriteAllBytes(archive,Zip("f.txt","UPDATED"));
Check("UNZIP_OVERWRITE",QuantConnect.Compression.Unzip(archive,outDir,true)&&File.ReadAllText(Path.Combine(outDir,"f.txt"))=="UPDATED");
Console.WriteLine("QL7_RESULT="+JsonSerializer.Serialize(new{rows,security_or_pin_accepted=false}));
