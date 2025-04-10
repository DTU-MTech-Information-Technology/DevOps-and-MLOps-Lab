from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Define FastAPI app
app = FastAPI()

# Define a Pydantic model for input validation
class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define a prediction endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Convert the input data to a numpy array (model expects numpy arrays)
    input_features = np.array([[input_data.sepal_length, 
                                input_data.sepal_width, 
                                input_data.petal_length, 
                                input_data.petal_width]])

    # Get the model's prediction
    prediction = model.predict(input_features)

    # Return the prediction result
    return {"prediction": int(prediction[0])}
