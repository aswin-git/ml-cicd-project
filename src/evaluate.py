import sys
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

with open("artifacts/latest.txt") as f:
    version = f.read().strip()

model = joblib.load(f"artifacts/model_v{version}.pkl")

X_test = pd.read_csv("artifacts/X_test.csv")
y_test = pd.read_csv("artifacts/y_test.csv")

preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)

print(f"Model accuracy: {accuracy}")

THRESHOLD = 1.0

if accuracy < THRESHOLD:
    print("Accuracy below threshold. Pipeline failed.")
    sys.exit(1)

print("Model passed quality gate.")
