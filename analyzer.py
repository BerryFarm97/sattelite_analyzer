import matplotlib.pyplot as plt


def print_summary(data):
    print("=== SATELLITE TELEMETRY SUMMARY ===")
    print(f"Average Battery: {data['battery_percent'].mean():.2f}%")
    print(f"Max Temperature: {data['temperature_c'].max():.2f}°C")
    print(f"Min Altitude: {data['altitude_km'].min():.2f} km")
    print(f"Lowest Signal Strength: {data['signal_strength'].min():.2f}%")


def check_health(data):
    print("\n⚠️⚠️⚠️ HEALTH WARNINGS ⚠️⚠️⚠️")

    if data['battery_percent'].min() < 25:
        print(f"🔋BATTERY LOW!🔋 BATTERY: {data['battery_percent'].mean():.2f}%")
    
    if data['temperature_c'].max() > 75:
        print(f"🔥TEMPS HIGH!🔥 TEMP: {data['temperature_c'].max():.2f}°C")

    if data['signal_strength'].min() < 60:
        print(f"📡WEAK SIGNAL!📡 SIGNAL: {data['signal_strength'].min():.2f}%")



def plot_temps(data):
    plt.plot(data["timestamp"], data["temperature_c"])
    plt.title("Satellite Temperature Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.show()

def generate_report(data):
    with open("health_report.txt", "w") as file:
        file.write("=== SATELLITE HEALTH REPORT === \n\n")
        file.write(f"Average Battery: {data['battery_percent'].mean():.2f}%\n")
        file.write(f"Max Temperature: {data['temperature_c'].max():.2f}°C\n")
        file.write(f"Min Altitude: {data['altitude_km'].min():.2f}km\n")
        file.write(f"Lowest Signal Strength: {data['signal_strength'].min():.2f}%\n")
        if data["battery_percent"].min() < 25:
            file.write(f"🔋BATTERY LOW!🔋 BATTERY: {data['battery_percent'].mean():.2f}%\n")
        if data["temperature_c"].max() > 70:
            file.write(f"🔥TEMPS HIGH!🔥 TEMP: {data['temperature_c'].max():.2f}°C\n")
        if data["signal_strength"].min() < 60:
            file.write(f"📡WEAK SIGNAL!📡 SIGNAL: {data['signal_strength'].min():.2f}%\n")