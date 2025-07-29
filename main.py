import pandas as pd
from analyzer import print_summary, check_health

def load_telemetry_data(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=['timestamp'])
        print("Telemetry data loaded successfully!\n")
        return df
    except FileNotFoundError:
        print("Telemetry file not found.")
        return None

def main():
    file_path = "telemetry.csv"
    data = load_telemetry_data(file_path)
    
    if data is not None:
        print(data.head())  # Show first few rows
        print_summary(data)
        check_health(data)

if __name__ == "__main__":
    main()
