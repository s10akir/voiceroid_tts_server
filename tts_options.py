from typing import Optional
from pydantic import BaseModel


class TTSOptions(BaseModel):
    language: str
    voice: str
    text: str
    speed: Optional[float] = None  # TODO: validation 0.5 ~ 4.0
    pitch: Optional[float] = None  # TODO: validation 0.5 ~ 2.0
