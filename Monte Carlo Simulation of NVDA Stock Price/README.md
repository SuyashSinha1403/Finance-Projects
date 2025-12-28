# Monte Carlo Simulation of NVDA Stock Price

**Date:** 28 December 2025  

 Project Overview
This project uses Monte Carlo simulation based on Geometric Brownian Motion (GBM) to model
possible future price paths for NVIDIA (NVDA) stock over a short-term horizon.

Instead of producing a single target price, the model generates a distribution of outcomes
to quantify upside potential and downside risk.

 Methodology
- Historical daily returns used to estimate drift (μ) and volatility (σ)
- Stock prices simulated using GBM
- 10,000 Monte Carlo simulations
- 22 trading-day forecast horizon (1-month)
- Percentile analysis (P10, P50, P90)
- Probability-based risk metrics
  
Key Outputs
- Simulated price paths
- Most likely (median) price trajectory
- Distribution of final prices
- Downside and upside probabilities

 Sample Risk Metrics
- P10 (Downside scenario)
- P50 (Median outcome)
- P90 (Upside scenario)
- Probability of price exceeding key thresholds

