# routes/models.py

from pydantic import BaseModel


class AddNumbers(BaseModel):
    number1: float
    number2: float
