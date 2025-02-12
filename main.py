from fastapi import FastAPI
from pydantic import BaseModel
import autocomplete_trie

app = FastAPI()

class InputData_buy(BaseModel):
    text: str

class InputData_sell(BaseModel):
    texts: list[str]
    query: str

@app.post("/autocomplete_buy/")
def predict(data: InputData_buy):
    result = autocomplete_trie.get_suggestions_api_buy(data.text)  # Call your function
    return {"suggestions": result}

@app.post("/autocomplete_sell/")
def predict(data: InputData_sell):
    result = autocomplete_trie.get_suggestions_api_sell(data.query, data.texts)  # Call your function
    return {"suggestions": result}
