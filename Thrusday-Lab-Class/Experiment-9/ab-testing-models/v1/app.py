import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_FILE = "model_v1.pkl"

# Load the model
model = joblib.load(MODEL_FILE)
print(f"✅ Loaded model from: {MODEL_FILE}")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"version": 1, "prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def health_check():
    return f"🔁 Serving model: {MODEL_FILE}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
