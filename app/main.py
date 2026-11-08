from fastapi import FastAPI, HTTPException

from app.price import parse_price

app = FastAPI()

@app.get("/price")
def get_price(text: str):
    try:
        value = parse_price(text)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    return {"text": text, "price": value}