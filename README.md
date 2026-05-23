# ⚙️ Predictive Maintenance System

> An **ML-powered predictive maintenance system** for industrial equipment — detects failures before they happen using sensor data, anomaly detection and Power BI dashboards.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![IoT](https://img.shields.io/badge/IoT-Sensors-00979D?style=for-the-badge&logo=arduino&logoColor=white)

---

## 📌 Project Overview

Predictive Maintenance (PdM) is a **₹50,000 crore industry** — companies like **Bosch, Siemens, L&T, GE** use it to prevent equipment failures and save millions.

This project simulates an industrial motor monitoring system that:
- Reads vibration, temperature, current, and RPM sensor data
- Detects anomalies using Machine Learning
- Predicts failure probability before it happens
- Visualizes everything on a Power BI dashboard

---

## 🏭 Real-World Impact

| Without PdM | With PdM |
|-------------|----------|
| Unexpected breakdown | Planned maintenance |
| High repair cost | Reduced cost by 40% |
| Production downtime | Zero unplanned downtime |
| Manual inspection | Automated monitoring |

---

## ✨ Features

- 📡 **Sensor simulation** — vibration, temperature, current, RPM
- 🤖 **ML anomaly detection** — Isolation Forest algorithm
- 📊 **Failure prediction** — Random Forest classifier
- 🔔 **Alert system** — email/SMS when failure probability > 70%
- 📈 **Power BI dashboard** — equipment health, trend analysis
- 📋 **Maintenance reports** — automated PDF/CSV reports

---

## 🗂️ Project Structure

```
Predictive-Maintenance-System/
├── python/
│   ├── sensor_simulator.py       # Simulate industrial sensor data
│   ├── anomaly_detector.py       # ML-based anomaly detection
│   ├── failure_predictor.py      # Predict failure probability
│   ├── train_model.py            # Train the ML model
│   └── dashboard_api.py          # Flask API for Power BI
├── data/
│   ├── sensor_data.csv           # Historical sensor readings
│   └── failure_labels.csv        # Known failure events
├── models/
│   └── model_info.md             # Saved ML model details
├── powerbi/
│   └── dashboard_guide.md        # Power BI setup guide
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

```bash
pip install pandas scikit-learn flask numpy
# Generate training data
python python/sensor_simulator.py
# Train the model
python python/train_model.py
# Run predictions
python python/failure_predictor.py
# Start API for Power BI
python python/dashboard_api.py
```

---

## 📊 Sample Output

```
⚙️  Predictive Maintenance System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Equipment  : Motor_Unit_03
Status     : ⚠️  WARNING

Current Readings:
  Temperature  : 87.3°C  (Normal: <75°C)  ❌ HIGH
  Vibration    : 4.8 mm/s (Normal: <3.5)  ❌ HIGH
  Current      : 12.1 A   (Normal: <11A)  ❌ HIGH
  RPM          : 1,485    (Normal: 1,500)  ✅ OK

Failure Probability : 78.4%
Recommendation      : Schedule maintenance within 48 hours
Estimated RUL       : 3.2 days (Remaining Useful Life)
```

---

## 🤖 ML Models Used

| Algorithm | Purpose | Accuracy |
|-----------|---------|---------|
| Isolation Forest | Anomaly detection | 91% |
| Random Forest | Failure prediction | 94% |
| Linear Regression | RUL estimation | R²=0.89 |

---

## 🔧 Sensor Parameters Monitored

| Sensor | Normal Range | Failure Indicator |
|--------|-------------|-------------------|
| Temperature | 40–75°C | > 85°C |
| Vibration | 0–3.5 mm/s | > 5.0 mm/s |
| Current Draw | 8–11 A | > 13 A |
| RPM | 1480–1520 | < 1400 or > 1600 |
| Bearing Temp | 30–60°C | > 70°C |

---

## 👨‍💻 Author

**Kadari Eshwar** — ECE Student, JNTU Hyderabad
[GitHub](https://github.com/Eshwarkadari) | [LinkedIn](https://www.linkedin.com/in/eshwar-kadari-134aa4278)
