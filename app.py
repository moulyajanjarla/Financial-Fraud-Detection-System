import pickle
import numpy as np
from flask import Flask, request, jsonify

# Load the trained model
with open("fraud_detection_model .pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.json

        # Check if 'features' key is present
        if 'features' not in data:
            return jsonify({"error": "Missing 'features' in request data"}), 400
        
        features = np.array(data['features']).reshape(1, -1)

        # Ensure model is a scikit-learn classifier
        if not hasattr(model, "predict"):
            return jsonify({"error": "Loaded object is not a valid model"}), 400

        prediction = model.predict(features)[0]

        return jsonify({"fraud_prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
