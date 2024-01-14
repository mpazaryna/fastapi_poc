import os
from typing import Union

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from agents.add.adder import add_two_numbers


class AddNumbers(BaseModel):
    number1: float
    number2: float


# Load environment variables from .env file
load_dotenv()

CUSTOM_API_KEY = os.getenv("CUSTOM_API_KEY", "")

app = FastAPI()


def check_custom_api_key(request: Request):
    api_key = request.headers.get("X-Custom-API-Key")
    if api_key is None:
        raise HTTPException(status_code=401, detail="Missing API key")
    if api_key != CUSTOM_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/", dependencies=[Depends(check_custom_api_key)])
def read_root():
    return {"Hello": "World"}


@app.post("/add")
async def add(number1: float, number2: float):
    return {"result": add_two_numbers(number1, number2)}


@app.post("/v1/add", dependencies=[Depends(check_custom_api_key)])
async def add(number1: float, number2: float):
    return {"result": add_two_numbers(number1, number2)}


@app.post("/json/add")
async def add(add_numbers: AddNumbers):
    return {"result": add_two_numbers(add_numbers.number1, add_numbers.number2)}
