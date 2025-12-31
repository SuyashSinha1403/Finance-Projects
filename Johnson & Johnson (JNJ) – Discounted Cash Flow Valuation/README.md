# Johnson & Johnson (JNJ) – Discounted Cash Flow Valuation

## Project Overview
This project presents a bottom-up intrinsic valuation of Johnson & Johnson (JNJ) using a Discounted Cash Flow (DCF) framework. The objective is to estimate the intrinsic equity value per share based on normalized operating performance and long-term business fundamentals.

The model is designed with a clear separation between assumptions, operating forecasts, cash flow generation, and valuation outputs to ensure transparency and auditability.

## Methodology
The valuation follows a standard unlevered DCF approach:

- Forecast operating performance over a 5-year explicit period
- Compute unlevered free cash flows (UFCF)
- Discount cash flows using the Weighted Average Cost of Capital (WACC)
- Estimate terminal value using the Gordon Growth Model
- Convert enterprise value to equity value by adjusting for net debt
- Derive intrinsic value per share using diluted shares outstanding

This approach isolates operating performance from financing decisions and reflects long-run, sustainable cash generation.

## Model Structure
The Excel model is organized into clearly defined sections:

- **Assumptions**: Centralized sheet containing all operating, capital, and valuation assumptions
- **Operating Forecast**: Revenue, EBIT, depreciation, CapEx, and working capital projections
- **Free Cash Flow**: Computation of unlevered free cash flows
- **Discounting**: Present value of forecast cash flows and terminal value
- **EV to Equity Bridge**: Conversion of enterprise value to intrinsic equity value
- **Outputs**: Intrinsic value per share and valuation summary

All key assumptions are editable in the Assumptions sheet, enabling easy scenario and sensitivity analysis.


## Data Extraction & Preprocessing
Financial statements (Income Statement, Cash Flow Statement, and Balance Sheet) were programmatically extracted using Python via the `yfinance` library.

The extraction script:
- Pulls full historical financial statements from Yahoo Finance
- Formats year-wise columns
- Scales values to USD millions
- Exports cleaned data to Excel for downstream valuation modeling

This ensures data transparency, reproducibility, and a clear separation between data sourcing and valuation logic.


## Key Outputs
- Enterprise Value (EV)
- Equity Value
- Intrinsic Value per Share
- Sensitivity of valuation to discount rate and terminal growth assumptions
  
## Key Insights
- Valuation is highly sensitive to WACC and terminal growth assumptions, as expected for a mature large-cap company
- Conservative normalization choices lead to intrinsic values that may differ materially from current market prices
- The model focuses on sustainable cash flows rather than short-term accounting noise or one-off items

