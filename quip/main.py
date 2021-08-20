from typing import List

from fastapi import FastAPI


app =  FastAPI()


@app.get('/')
def root():
    return {'root': "API not accessible as this"}
