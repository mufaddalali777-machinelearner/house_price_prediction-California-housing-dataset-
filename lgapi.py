from fastapi import FastAPI, Path
from pydantic import BaseModel
import json
import numpy as np
from contextlib import asynccontextmanager
from pydantic import Field

with open("model_weights.json", "r") as f:
    params = json.load(f)

w = np.array(params["w"])
b = params["b"]
mu = np.array(params["mu"])
std = np.array(params["std"])
app = FastAPI()

print(mu)
class ModelInput(BaseModel):
    features : list[float] = Field(..., min_length=8, max_length= 8)

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model weights here so they are ready before the app starts
    with open("model_weights.json", "r") as f:
        params = json.load(f)
        ml_models["w"] = np.array(params["w"])
        ml_models["b"] = params["b"]
        ml_models["mu"] = np.array(params["mu"])
        ml_models["std"] = np.array(params["std"])
    yield

@app.post("/predictor")
def price_predictor(data : ModelInput):
    input_list = np.array(data.features)
    
    new = (input_list - mu)/std
    predictions = np.dot(w, new) + b
    
    
    return int(predictions)



