import string
from typing import Union

from fastapi import FastAPI

from read_data import ReadData

from urllib.parse import urlencode

app = FastAPI()

lilpa = ReadData()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{channel_id}/")
async def read_id(channel_id, id: str = "", word: str = ""):
    return {"data": lilpa.get_chat_data(channel_id, id, word)}

