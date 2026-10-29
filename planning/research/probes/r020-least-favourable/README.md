# E6 — least-favourable null screening, pre-execution protocol

2026-10-14. Follow-up to E5's incomplete all-null screening. M1 fixed, no marketdata, strategy, engine or own historical performance. Reuse E2 dependencies, no install/spend/global change. New immutable attempt; E5 not rerun/overwritten.

Prespecified alternative **percentile** intervals, block20, AR(0.4) Gaussian logreturns, common correlation0.8, n1008/burn512,160MC per three cases,999bootstrap draws, one-sided95%, seed20261016. Same CAGR/ES contrasts and fractional q95; false qualification bounded only when tests valid. Do not select margins or a method because a strategy passes.

Cases NI_NULL (gS.07/gB.08/cash0), CASH_NULL (gS.04/gB0/cash.03), ES_NULL (gS.12/gB.02/cash.02). Synthetic M g.04/sigma.004; Ssigma solved **before samples** to .4ES(M) in NI/cash cases and .8ES(M) in ES case; Bsigma.008. Other population contrasts strictly positive, one selected contrast0. Report target-null rejection and AND plus MC Wilson95% uncertainty/errors. Other gates can still fail from finite uncertainty; AND0 never validates the marginal null or whole family.

This is **screening only** (not full-calibration): one DGP family, fixed block,160MC/999 draws do not establish rare-family error, real dependence/heavy tails/regimes, actual sample power or guardrail uncertainty. Record observed exceptions/invalid values in denominator. If inadequate, method NOT_ACCEPTED, M1 unchanged. No silent switch to percentile as approved final method.
