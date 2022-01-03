from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pyvcroid2 import VcRoid2

app = FastAPI()


@app.get("/")
async def redirect_docs():
    return RedirectResponse("/docs")
