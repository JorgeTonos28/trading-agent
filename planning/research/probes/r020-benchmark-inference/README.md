# E4 — benchmark arithmetic and inference pilot, preregistered

2026-10-14. Disposable research only, synthetic assets/returns, no prices downloaded or strategy backtest. Reuse local numpy/arch8/statsmodels0.15 dependencies from E2. No new installation, credentials, account, API, admin or configuration.

## Fixed scope before execution

Check arithmetic of buy-and-hold drift versus reset, reinvest distributions in the paying asset without restoring weights, split neutrality, dividend receivable versus available cash and delayed reinvest, cost charged once, exposure versus factor/beta difference. These are standalone calculations, not an engine, broker model or production validator.

Empirical ES uses loss=-return, fractional upper-tail weights (no clipping and no tie overcount). Check fractional case/ties, ES difference versus ES of paired difference, nonpositive reference, all-constant and nonfinite `conf_int` behavior. Retain actual library outcomes/errors, not just desired PASS. Source/result immutable; no rerun to improve outcomes.

Inference pilot fixed settings: seed20261014, 160 Monte Carlo replications per DGP, n1008 after burn512, 499 stationary-bootstrap draws, basic one-sided lower bound, size0.95. Compare block1 and block20 for IID normal, AR(0.6), and deterministic two-volatility-regime normal innovations (sigma0.0008, regime factor4). DGP true annual mean paired difference0, synthetic NI margin1pp; report boundary rejection with shifted contrast0 and power at true difference0. No CAGR, ES, joint-gate or regime-validity coverage is established by this mean primitive. Regime case deliberately stresses stationarity; neither block selected from resulting rates.

Report Monte Carlo counts and Wilson95% uncertainty; nominal rates are observations, not calibrated-method PASS. Fixed drift/no observed-market fitting; tiny pilot cannot certify rare-error control across scenarios. No trading alpha or PRICE/MATR sample sufficiency estimates. All fixture numbers, tail0.95, margin1pp, block/reps/alpha remain proposals/illustrations, not owner-approved economic parameters.

Output records source SHA, versions, checks, degenerate observations, pilot results and limitations. Launch with private HOME, environment allowlist and Python network guard; this is not OS security. Fresh clone must reconstruct dependencies and emit new attempt; never overwrite the captured result.
