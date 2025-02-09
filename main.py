from fastapi import FastAPI
from pydantic import BaseModel
import autocomplete_trie

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/autocomplete/")
def predict(data: InputData):
    result = autocomplete_trie.get_suggestions_api(data.text)  # Call your function
    return {"suggestions": result}
