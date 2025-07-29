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