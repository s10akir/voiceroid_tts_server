from fastapi import FastAPI
from pyvcroid2 import VcRoid2

app = FastAPI()
vc = VcRoid2()


@app.get("/")
async def root():
    languages = vc.listLanguages()
    voices = vc.listVoices()

    return {"languages": languages, "voices": voices}
