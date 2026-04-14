import csv
import os

def export_results(input_path, output_dir):

    max_price = float('-inf')
    min_price = float('inf')

    max_row = None
    min_row = None

    all_dates = []

    # -----------------------
    # Read cleaned data
    # -----------------------
    with open(input_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                date = row["Date"]
                open_price = float(row["Open"])
                high = float(row["High"])
                low = float(row["Low"])
                close = float(row["Close"])
                volume = float(row["Volume"])

                all_dates.append(date)

                # Highest (use High)
                if high > max_price:
                    max_price = high
                    max_row = {
                        "type": "highest",
                        "date": date,
                        "open": open_price,
                        "high_or_low": high,
                        "close": close,
                        "volume": volume
                    }

                # Lowest (use Low)
                if low < min_price:
                    min_price = low
                    min_row = {
                        "type": "lowest",
                        "date": date,
                        "open": open_price,
                        "high_or_low": low,
                        "close": close,
                        "volume": volume
                    }

            except Exception:
                continue

    # -----------------------
    # Handle empty case
    # -----------------------
    if not all_dates:
        print("No valid data")
        return

    start_date = min(all_dates)
    end_date = max(all_dates)

    # -----------------------
    # Prepare output
    # -----------------------
    output_rows = [max_row, min_row]

    os.makedirs(output_dir, exist_ok=True)

    filename = f"{output_dir}/stock_analysis_{start_date}_to_{end_date}.csv"

    # -----------------------
    # Write CSV
    # -----------------------
    with open(filename, "w", newline="") as file:
        fieldnames = ["type", "date", "open", "high_or_low", "close", "volume"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Exported: {filename}")