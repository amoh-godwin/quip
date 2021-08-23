from typing import List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

import gif_access
from dependencies import gif_drive, gif_db


app =  FastAPI()
app.include_router(gif_access.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'root': "API not accessible as this"}


@app.get('/upload/gif')
def upload_gif():
    with open('static/index.html') as index:
        conts = index.read()

    return HTMLResponse(content=conts)
