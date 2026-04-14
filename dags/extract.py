import csv
import os
from airflow.models import Variable

def extract_data(input_path, output_path, window_size=100):
    
    # Get offset from Airflow Variable
    offset = int(Variable.get("stock_offset", default_var=0))
    
    extracted_rows = []
    
    with open(input_path, "r") as file:
        reader = csv.DictReader(file)
        
        # Skip already processed rows
        for _ in range(offset):
            next(reader, None)
        
        # Read next window
        for _ in range(window_size):
            try:
                row = next(reader)
                extracted_rows.append(row)
            except StopIteration:
                break
    
    # Save extracted data
    if extracted_rows:
        with open(output_path, "w", newline="") as out_file:
            writer = csv.DictWriter(out_file, fieldnames=extracted_rows[0].keys())
            writer.writeheader()
            writer.writerows(extracted_rows)
    
    # Update offset
    new_offset = offset + len(extracted_rows)
    Variable.set("stock_offset", str(new_offset))
    
    print(f"Processed rows: {offset} to {new_offset}")