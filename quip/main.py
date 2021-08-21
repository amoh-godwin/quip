from typing import List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import gif_access
from dependencies import gif_drive


app =  FastAPI()
app.include_router(gif_access.router)

@app.get('/')
def root():
    return {'root': "API not accessible as this"}


@app.get('/upload/gif')
def upload_gif():
    with open('static/index.html') as index:
        conts = index.read()

    return HTMLResponse(content=conts)
