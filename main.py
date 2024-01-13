import os
from typing import Union

from dotenv import load_dotenv
from fastapi import FastAPI, Query
from openai import OpenAI
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Now, you can safely load the OPENAI_API_KEY
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()


class Order(BaseModel):
    product: str
    units: int


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


def fetch_news():
    try:
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "What are some of the key events that happened in March 2021?",
                }
            ],
            model="gpt-4-1106-preview",
        )
    except Exception as e:
        print("Error while generating description:", str(e))
        return None
    return (
        completion.choices[0].message.content if completion else "No response generated"
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/news")
def generate_news():
    news = fetch_news()
    return {"news": news}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
