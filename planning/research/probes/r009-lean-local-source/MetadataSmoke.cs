using System;
using System.Linq;
using System.Reflection;
using System.Text.Json;

// Metadata/type-load probe only. Never invoke the native Launcher entrypoint.
var rows = new System.Collections.Generic.List<object>();
void Check(string id, bool value) => rows.Add(new { id, status = value ? "PASS" : "FAIL" });
var host = Assembly.Load("LeanLocalSourceHostProbe");
Check("NATIVE_ENTRYPOINT_COMPILED_NOT_INVOKED", host.EntryPoint?.Name == "Main" && host.EntryPoint?.DeclaringType?.FullName == "QuantConnect.Lean.Launcher.Program");
foreach (var item in new[] {
    ("QuantConnect.Lean.Engine", "QuantConnect.Lean.Engine.Engine"),
    ("QuantConnect.Queues", "QuantConnect.Queues.JobQueue"),
    ("QuantConnect.Messaging", "QuantConnect.Messaging.Messaging"),
    ("QuantConnect.Common", "QuantConnect.Packets.BacktestNodePacket") })
{
    var asm = Assembly.Load(item.Item1);
    Check("TYPE_LOAD_" + item.Item2, asm.GetType(item.Item2, throwOnError: true) is not null);
}
Check("NO_CLI_ASSEMBLY_REFERENCE", !host.GetReferencedAssemblies().Any(x => x.Name == "Lean.Cli"));
Console.WriteLine("QL3_RESULT=" + JsonSerializer.Serialize(new { rows, entrypoint_invoked = false, engine_run = false }));
