import string

from fastapi import FastAPI

from data import GetData

from fastapi.middleware.cors import CORSMiddleware
# https://stackoverflow.com/questions/65635346/how-can-i-enable-cors-in-fastapi 
app = FastAPI()

data = GetData('./channels/')


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/videos/{channel_id}")
async def read_videos(channel_id):
    return {"list": data.get_video_list(channel_id)}


@app.get("/{channel_id}/videos/{videoid}/")
async def read_id(channel_id, videoid, search: str = "바보"):
    return {"data": data.get_chat_data(channel_id, videoid, search)}

