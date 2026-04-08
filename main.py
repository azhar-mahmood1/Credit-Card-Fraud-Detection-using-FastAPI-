from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model once at startup
model = joblib.load("fraud_model.pkl")

FEATURES = [f"V{i}" for i in range(1, 29)] + ["Amount"]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "features": FEATURES,
            "result": None,
            "form_values": {}
        }
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form_data = await request.form()

    try:
        values = [float(form_data.get(feat, 0)) for feat in FEATURES]
        input_array = np.array(values).reshape(1, -1)

        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0]

        confidence = round(float(max(probability)) * 100, 2)
        is_fraud = bool(prediction == 1)

        result = {
            "is_fraud": is_fraud,
            "label": "FRAUDULENT" if is_fraud else "LEGITIMATE",
            "confidence": confidence,
            "fraud_prob": round(float(probability[1]) * 100, 2),
            "legit_prob": round(float(probability[0]) * 100, 2),
        }

    except Exception as e:
        result = {"error": str(e)}

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "features": FEATURES,
            "result": result,
            "form_values": dict(form_data)
        }
    )