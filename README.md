# Satellite Data Analyzer

A Python-based command-line tool that simulates satellite telemetry monitoring. It loads telemetry data from a CSV file, summarizes key system health stats, detects potential risks, visualizes temperature trends, and generates a health report in text format.


## Features

- Loads real-time-style telemetry data from `telemetry.csv`
- Prints summary statistics (battery, temp, altitude, signal)
- Detects and reports system warnings:
  - Low battery
  - High temperature
  - Weak signal strength
- Generates a readable `.txt` health report
- Visualizes temperature data over time using matplotlib


## How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/BerryFarm97/satellite_analyzer.git
   cd satellite_analyzer

python -m venv venv
.\venv\Scripts\activate    # For Windows

pip install pandas matplotlib

python main.py


## Technologies Used

- Python 3.11
- pandas – for data loading and analysis
- matplotlib – for temperature trend visualization


## Future Improvements

- Add more telemetry visualizations (e.g. battery, signal)
- Create a live simulation mode with timed data updates
- Export reports in CSV or JSON format
- Add command-line options for selecting output types
- Build a GUI using Tkinter or PyQt (for future visual polish)


## License

This project is open-source and available for educational or personal use.
