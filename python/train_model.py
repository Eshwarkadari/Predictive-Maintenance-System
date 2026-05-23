"""
train_model.py  —  Train ML Models for Failure Prediction
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
Models: Isolation Forest (anomaly) + Random Forest (prediction)
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle, os

FEATURES = ["temperature", "vibration", "current", "rpm", "bearing_temp"]
TARGET   = "failure"

def train():
    print("📂 Loading sensor data...")
    df = pd.read_csv("../data/sensor_data.csv")
    print(f"   {len(df):,} records loaded")

    X = df[FEATURES]
    y = df[TARGET]

    # ── Isolation Forest (Anomaly Detection) ──────────────────
    print("\n🤖 Training Isolation Forest (Anomaly Detection)...")
    iso_forest = IsolationForest(contamination=0.05, random_state=42, n_estimators=100)
    scaler     = StandardScaler()
    X_scaled   = scaler.fit_transform(X)
    iso_forest.fit(X_scaled)

    anomaly_scores = iso_forest.decision_function(X_scaled)
    df["anomaly_score"] = anomaly_scores
    df["is_anomaly"]    = (iso_forest.predict(X_scaled) == -1).astype(int)
    anomaly_rate = df["is_anomaly"].mean() * 100
    print(f"   Anomaly rate detected: {anomaly_rate:.1f}%")

    # ── Random Forest (Failure Prediction) ───────────────────
    print("\n🤖 Training Random Forest (Failure Prediction)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

    rf_model = RandomForestClassifier(
        n_estimators=100, max_depth=10, random_state=42, class_weight="balanced")
    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X_test)
    acc    = accuracy_score(y_test, y_pred)
    print(f"   Accuracy: {acc*100:.1f}%")
    print("\n" + classification_report(y_test, y_pred, target_names=["Normal","Failure"]))

    # Feature importance
    print("   Feature Importance:")
    for feat, imp in sorted(zip(FEATURES, rf_model.feature_importances_),
                             key=lambda x: -x[1]):
        bar = "█" * int(imp * 30)
        print(f"     {feat:<15} {bar} {imp:.3f}")

    # Save models
    os.makedirs("../models", exist_ok=True)
    with open("../models/rf_model.pkl",  "wb") as f: pickle.dump(rf_model, f)
    with open("../models/iso_model.pkl", "wb") as f: pickle.dump(iso_forest, f)
    with open("../models/scaler.pkl",    "wb") as f: pickle.dump(scaler, f)
    print("\n✅ Models saved to models/")

if __name__ == "__main__":
    train()
