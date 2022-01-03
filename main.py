from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from pyvcroid2 import VcRoid2
from tts_options import TTSOptions

app = FastAPI()


@app.get("/")
async def redirect_docs():
    return RedirectResponse("/docs")


@app.get("/info")
async def info():
    vc = VcRoid2()

    return {"languages": vc.listLanguages(), "voice": vc.listVoices()}


@app.post("/tts")
async def tts(tts_options: TTSOptions):
    vc = VcRoid2()
    vc.loadLanguage(tts_options.language)
    vc.loadVoice(tts_options.voice)

    speach, _ = vc.textToSpeech(tts_options.text)

    return Response(content=speach, media_type="audio/wave")
