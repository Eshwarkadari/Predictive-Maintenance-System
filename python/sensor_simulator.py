"""
sensor_simulator.py  —  Industrial Sensor Data Generator
Simulates motor sensors: temperature, vibration, current, RPM
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sensor_data(n_days=180, machines=5):
    """Generate realistic industrial sensor data with failures."""
    records = []
    start   = datetime(2024, 1, 1)

    for machine_id in range(1, machines + 1):
        # Each machine has a random failure point
        failure_day   = random.randint(120, 175)
        failure_start = random.randint(100, failure_day - 5)

        for day in range(n_days):
            for hour in range(0, 24, 2):  # Every 2 hours
                ts = start + timedelta(days=day, hours=hour)

                # Degradation factor (increases as failure approaches)
                if day < failure_start:
                    deg = 0.0
                elif day < failure_day:
                    deg = (day - failure_start) / (failure_day - failure_start)
                else:
                    deg = 1.0

                failed = day >= failure_day

                records.append({
                    "timestamp":    ts.strftime("%Y-%m-%d %H:%M:%S"),
                    "machine_id":   f"Motor_Unit_{machine_id:02d}",
                    "temperature":  round(45 + 30 * deg + np.random.normal(0, 2), 1),
                    "vibration":    round(1.5 + 3.5 * deg + np.random.normal(0, 0.2), 2),
                    "current":      round(9.0 + 4.5 * deg + np.random.normal(0, 0.3), 2),
                    "rpm":          round(1500 - 100 * deg + np.random.normal(0, 10)),
                    "bearing_temp": round(35 + 25 * deg + np.random.normal(0, 1.5), 1),
                    "degradation":  round(deg, 3),
                    "failure":      int(failed),
                    "rul_days":     max(0, failure_day - day)
                })

    df = pd.DataFrame(records)
    df.to_csv("../data/sensor_data.csv", index=False)
    print(f"✅ Generated {len(df):,} sensor readings for {machines} machines")
    print(f"   Saved to data/sensor_data.csv")
    return df

if __name__ == "__main__":
    df = generate_sensor_data()
    print(df.tail())
