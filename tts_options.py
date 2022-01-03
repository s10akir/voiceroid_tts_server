from pydantic import BaseModel


class TTSOptions(BaseModel):
    language: str = "standard"
    voice: str = "aoi_emo_44"
    text: str
