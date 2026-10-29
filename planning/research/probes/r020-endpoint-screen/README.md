# E5 — screening of CAGR/ES uncertainty, protocol before execution

2026-10-14. Disposable synthetic statistics only; no Trading OS/strategy/backtest/data/provider calls. Reuse E2 numpy/arch8/statsmodels0.15, no installation or global config. M1 utilities fixed; no grid/optimization of margins.

Fixed pilot:80MonteCarlo samples per DGP,1008synthetic sessions after burn512,499 stationary draws, block20, basic one-sided95% bounds, seed20261015. IID and Gaussian AR(0.4) multivariate log returns, common innovation correlation0.8. Population long-run CAGR B=.06, S=.05, cash=.04; M=.04 and daily log sigmaM=.004, sigmaB=.008. Solve sigmaS analytically before any sample so population ES(S)=.8ES(M). All three utility contrasts are exactly at null boundaries. M is a synthetic statistical reference, **not an accepted lambda portfolio or K2 implementation**.

ES of daily loss=1-exp(logreturn), fractional worst5% mass, no clipping. Theoretical lower-lognormal-tail mean uses normalCDF; retain population constants/solver residual. Contrasts: CAGR(S)-CAGR(B)+.01; CAGR(S)-CASH-.01; .8ES(M)-ES(S). Same resampling indices, all-positive lower bounds for qualification, no separate favorable metric selection. Report rejection per endpoint, AND, Wilson95% MC uncertainty and errors. Treat errors as failed/unavailable inference, not drop them from denominator.

Check population boundaries, fractional/tie ES, finite inputs, and recovery censoring on a small deterministic equity path. Drawdown/recovery checks are arithmetic only, not confidence intervals. Synthetic annualization252 equals an ideal four-year convention here, not the actual calendar or historical strategy sample. Independent cases not firm-level trade count.

Pilot is **screening only**, not final method acceptance:80samples and499draws cannot validate family-level low-tail bounds, nonstationarity, rare gaps, real tail clustering, CAGR/ES/DD joint guarantees or target runtime. No parameter changed to improve outcomes. Full calibration protocol must require MonteCarlo precision and scenario coverage before PASS, even if these fixtures all succeed.

Private HOME/envallowlist/Python network guard, immutable source/result/launcher/dependency evidence. Do not repeat/overwrite capture to improve rates.
