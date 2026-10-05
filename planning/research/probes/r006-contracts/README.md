# R-006 contracts — disposable planning probes

No Trading OS implementation, broker/order endpoint, production runtime or paid API. These fixtures exercise the contract spine, not the entire final financial/pedagogical system. Schemas are illustrative RC0 instantiations; narrative claims still need review. Historical wave 04 artifacts are immutable inputs.

- `make_fixtures.py`: constructs role-specific JSON schemas and synthetic evidence/examples (stdlib only).
- `admission_probe.py`: uses public jsonschema and Decimal for targeted negative admission checks, paired delivery states and replay.
- `behavior_probe.py`: reuses wave 04 native transport helper, only synthetic read_evidence; fixed Team/native auth. New corrected procedures are scoped to this experiment.
- `evaluate.py`: evaluates saved synthetic behavior outputs; no inference or order effect.
- `result-local.json`, `result-team-attempt-01.json`, `evaluation-team.json`: observed results after execution, not expected results.
- `result-local-v2.json`: 39/39 after qualified citation clarification; original 36/36 retained. `evaluation-team.json` preserves v1 (8/10) vs v2 (10/10) admission, not an entirely preregistered 10/10 claim.
- `codex_sdk_probe.py`, `result-codex-sdk-attempt-01/02.json`: official native SDK smoke, first harness enum error before inference retained, second 7/7; never Agents SDK paid API. SDK wheel/packaging/pydantic are temporal dependencies, CLI override explicit. Dynamic callbacks/full Skills/state/Plus not proved.

Run from this directory using Python with the research temp dependencies (`jsonschema 4.26.0`, PyYAML for Skill validation). Do not copy auth/config into the repository. There is no requirement to install anything globally or in target Plus. See `R-006_probe_wave_06_protocol.md` and the three planning contracts for semantics and limitations.
