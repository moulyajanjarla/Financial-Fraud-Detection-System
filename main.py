from fastapi import FastAPI, HTTPException
import numpy as np
import pickle
from pydantic import BaseModel

# Load the trained model
with open("fraud_detection_model .pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize FastAPI app
app = FastAPI()

# Define request body model
class FraudRequest(BaseModel):
    features: list

@app.post("/predict")
def predict(request: FraudRequest):
    try:
        features = np.array(request.features).reshape(1, -1)
        prediction = model.predict(features)[0]
        return {"fraud_prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
