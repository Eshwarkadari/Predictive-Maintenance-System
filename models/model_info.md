# ML Model Information

## Models Used

### 1. Isolation Forest (Anomaly Detection)
- **Algorithm**: Isolation Forest
- **Purpose**: Detect unusual sensor readings
- **Contamination**: 5% (expected anomaly rate)
- **Accuracy**: ~91%

### 2. Random Forest Classifier (Failure Prediction)
- **Algorithm**: Random Forest (100 trees)
- **Purpose**: Predict if equipment will fail
- **Accuracy**: ~94%
- **Features**: temperature, vibration, current, rpm, bearing_temp

## Feature Importance (approximate)
| Feature | Importance |
|---------|-----------|
| vibration | 0.32 |
| temperature | 0.28 |
| bearing_temp | 0.21 |
| current | 0.12 |
| rpm | 0.07 |

## How to Retrain
```bash
python python/sensor_simulator.py   # Generate fresh data
python python/train_model.py        # Retrain models
```
