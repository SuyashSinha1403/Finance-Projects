import yfinance as yf
import pandas as pd

# TICKER
TICKER = "JNJ"   

ticker = yf.Ticker(TICKER)

# LOAD FULL STATEMENTS
income = ticker.financials         
cashflow = ticker.cashflow          
balance_sheet = ticker.balance_sheet  

# FORMAT YEARS (COLUMNS)
def clean_columns(df):
    df = df.copy()
    df.columns = pd.to_datetime(df.columns).year
    df = df.sort_index(axis=1)
    return df

income = clean_columns(income)
cashflow = clean_columns(cashflow)
balance_sheet = clean_columns(balance_sheet)


# SCALE TO USD MILLIONS 
income /= 1e6
cashflow /= 1e6
balance_sheet /= 1e6

# EXPORT TO EXCEL
file_name = f"{TICKER}_FULL_IS_CF_BS.xlsx"

with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
    income.to_excel(writer, sheet_name="Income_Statement_FULL")
    cashflow.to_excel(writer, sheet_name="Cash_Flow_FULL")
    balance_sheet.to_excel(writer, sheet_name="Balance_Sheet_FULL")

print("✅ Full financial statements extracted successfully")
print(f"📁 File saved as: {file_name}")
print(f"📊 Years available: {list(income.columns)}")
