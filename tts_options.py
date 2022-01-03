from pydantic import BaseModel
from pyvcroid2 import VcRoid2


class TTSOptions(BaseModel):
    language: str
    voice: str
    text: str
