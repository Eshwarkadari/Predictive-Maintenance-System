"""
failure_predictor.py  —  Real-time Failure Prediction
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
"""

import pandas as pd
import numpy as np
import pickle

FEATURES = ["temperature", "vibration", "current", "rpm", "bearing_temp"]
NORMALS  = {
    "temperature":   (40, 75),
    "vibration":     (0,  3.5),
    "current":       (8,  11),
    "rpm":           (1480, 1520),
    "bearing_temp":  (30, 60),
}

def load_models():
    with open("../models/rf_model.pkl",  "rb") as f: rf  = pickle.load(f)
    with open("../models/iso_model.pkl", "rb") as f: iso = pickle.load(f)
    with open("../models/scaler.pkl",    "rb") as f: sc  = pickle.load(f)
    return rf, iso, sc

def predict(readings: dict):
    """Predict failure probability for a set of sensor readings."""
    try:
        rf, iso, scaler = load_models()
    except FileNotFoundError:
        print("⚠️  Models not found. Run train_model.py first.")
        return

    X = pd.DataFrame([readings])[FEATURES]
    X_scaled = scaler.transform(X)

    failure_prob  = rf.predict_proba(X)[0][1]
    is_anomaly    = iso.predict(X_scaled)[0] == -1
    anomaly_score = iso.decision_function(X_scaled)[0]

    # Estimate RUL
    rul = max(0, round((1 - failure_prob) * 10, 1))

    print("\n⚙️  Predictive Maintenance System")
    print("━" * 40)
    print(f"Equipment : {readings.get('machine_id', 'Unknown')}")

    status = "✅ NORMAL" if failure_prob < 0.3 else ("⚠️  WARNING" if failure_prob < 0.7 else "🚨 CRITICAL")
    print(f"Status    : {status}\n")
    print("Sensor Readings:")
    for sensor, value in readings.items():
        if sensor == "machine_id": continue
        lo, hi = NORMALS.get(sensor, (0, 9999))
        ok = "✅ OK" if lo <= value <= hi else "❌ OUT OF RANGE"
        print(f"  {sensor:<15} {value:>8}  {ok}")

    print(f"\nFailure Probability : {failure_prob*100:.1f}%")
    print(f"Anomaly Detected    : {'Yes ⚠️' if is_anomaly else 'No ✅'}")
    print(f"Estimated RUL       : {rul} days")

    if failure_prob > 0.7:
        print("\n🔧 Recommendation: IMMEDIATE maintenance required!")
    elif failure_prob > 0.4:
        print("\n🔧 Recommendation: Schedule maintenance within 48 hours.")
    else:
        print("\n🔧 Recommendation: Continue normal operation.")

if __name__ == "__main__":
    # Simulate a degrading motor
    test_readings = {
        "machine_id":   "Motor_Unit_03",
        "temperature":  87.3,
        "vibration":    4.8,
        "current":      12.1,
        "rpm":          1485,
        "bearing_temp": 68.5,
    }
    predict(test_readings)
