from typing import List

from fastapi import FastAPI

import gif_drive
from dependencies import gif_drive


app =  FastAPI()
app.include_router(gif_drive.router)

@app.get('/')
def root():
    return {'root': "API not accessible as this"}
