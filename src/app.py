import time
import joblib
from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, generate_latest

with open("artifacts/latest.txt") as f:
    version = f.read().strip()

model = joblib.load(f"artifacts/model_v{version}.pkl")

app = Flask(__name__)

REQUESTS = Counter(
    "prediction_requests_total",
    "Total prediction requests"
)

LATENCY = Histogram(
    "prediction_latency_seconds",
    "Prediction latency"
)

@app.route("/predict", methods=["POST"])
def predict():
    start = time.time()
    REQUESTS.inc()

    features = request.json["features"]
    prediction = model.predict([features]).tolist()

    LATENCY.observe(time.time() - start)

    return jsonify({
        "model_version": version,
        "prediction": prediction
    })

@app.route("/metrics")
def metrics():
    return generate_latest()

app.run(host="0.0.0.0", port=5000)
