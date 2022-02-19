"""
    Schema for the API.
"""
  
from pydantic import BaseModel, conlist
from typing import List, Any


class Image(BaseModel):
    data: List[conlist(float, min_items=4, max_items=4)]


class IrisPredictionResponse(BaseModel):
    prediction: Any
    probability: List[Any]
    log_probability: List[Any]