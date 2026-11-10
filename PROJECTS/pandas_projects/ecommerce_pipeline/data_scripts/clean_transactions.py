import pandas as pd
import numpy as np

def run_pipeline():
    print("--- 1. INGESTING RAW TRANSACTION DATA ---")
    
    # Simulating a messy real world e-commerce transaction dataset
    raw_data = {
        'transaction_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
        'customer_name': ['  Fidha S. ', 'Krishnendu ', '  parvathi', 'Anu A.', '   ', np.nan, 'Ganga S.  '],
        'order_date': ['2026-11-01', '02/11/2026', '2026-11-03', 'InvalidDate', '2026-11-05', '2026-11-06', '2026-11-07'],
        'category': ['Electronics', '  home ', 'electronics', 'BEAUTY', 'Home', '  Fashion ', 'Electronics'],
        'amount': [1250.00, np.nan, 450.50, 89.00, 210.00, np.nan, 3100.00],
        'status': ['Completed', 'completed', ' Pending', 'Completed', 'Cancelled', 'Completed', ' Completed ']
    }

    df = pd.DataFrame(raw_data)
    print("Raw DataFrame shape:", df.shape)
    print(df.head(3))
    print("\n" + "*"*50 + "\n")

    print("--- 2. CLEANING TEXT & CATEGORICAL COLUMNS ---")
    
    # Remove rows where customer_name is missing or just empty whitespace
    df['customer_name'] = df['customer_name'].astype(str).str.strip()
    df = df[df['customer_name'] != '']
    df = df[df['customer_name'] != 'nan']
    df['customer_name'] = df['customer_name'].str.title()  # Fix capitalisation (e.g. 'parvathi' -> 'Parvathi')

    # Standardise categories and status strings
    df['category'] = df['category'].str.strip().str.capitalize()
    df['status'] = df['status'].str.strip().str.capitalize()

    print("--- 3. HANDLING MISSING AMOUNTS & INVALID DATES ---")
    
    # Convert dates: 'errors="coerce"' turns unparseable text like 'InvalidDate' into NaT (Not a Time)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    # Fill missing sales amounts with the median category price instead of a global average
    median_amount = df['amount'].median()
    df['amount'] = df['amount'].fillna(median_amount)

    print("--- 4. FEATURE ENGINEERING ---")
    
    # Calculate high-value order flag using a boolean condition
    df['is_high_value'] = df['amount'] > 500.0

    print("\n--- CLEANED DATASET READY ---")
    print(df)
    print("\nDataFrame Info:")
    print(df.info())

    # Save the cleaned data to a CSV in your data folder
    df.to_csv('../data/cleaned_transactions.csv', index=False)
    print("\nCleaned file saved to data/cleaned_transactions.csv!")

if __name__ == '__main__':
    run_pipeline()