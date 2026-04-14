import csv
import pandas as pd

def transform_data(input_path, output_path):
    
    cleaned_rows = []

    with open(input_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                # -----------------------
                # 1. Remove whitespace
                # -----------------------
                row = {k: v.strip() for k, v in row.items()}

                # -----------------------
                # 2. Convert Date
                # -----------------------
                date = pd.to_datetime(row["Date"], errors="coerce")

                if pd.isna(date):
                    continue

                # -----------------------
                # 3. Validate numeric fields
                # -----------------------
                open_price = float(row["Open"])
                high = float(row["High"])
                low = float(row["Low"])
                close = float(row["Close"])
                volume = float(row["Volume"])
                dividends = float(row["Dividends"])
                splits = float(row["Stock Splits"])

                # -----------------------
                # 4. Remove invalid values
                # -----------------------
                if (
                    open_price <= 0 or
                    high <= 0 or
                    low <= 0 or
                    close <= 0
                ):
                    continue

                # -----------------------
                # 5. Store cleaned row
                # -----------------------
                cleaned_rows.append({
                    "Date": date,
                    "Open": open_price,
                    "High": high,
                    "Low": low,
                    "Close": close,
                    "Volume": volume,
                    "Dividends": dividends,
                    "Stock Splits": splits
                })

            except Exception:
                # Skip invalid rows
                continue

    # -----------------------
    # Save cleaned data
    # -----------------------
    if cleaned_rows:
        df = pd.DataFrame(cleaned_rows)
        df.to_csv(output_path, index=False)

    print(f"Cleaned rows count: {len(cleaned_rows)}")