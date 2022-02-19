"""
    Schema for the API.
"""
from pydantic import BaseModel

class OutputImage(BaseModel):
    """
    Schema for the output.
    """

    image: bytes
