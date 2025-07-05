from fastapi import FastAPI, Request
from pydantic import BaseModel
from Fully_Working import run_inference  # Modify to expose a callable function

app = FastAPI()

class TextInput(BaseModel):
    text: str
@app.post("/analyze/")
from Fully_Working import run_inference_on_text

@app.post("/analyze/")
def analyze_text(input: TextInput):
    result = run_inference_on_text(input.text)
    return result
