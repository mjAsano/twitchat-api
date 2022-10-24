# twitchat-api
rest api for analyze twitch chat. dataset is fit with pypi.org/project/tcd costom config

## Requirement
```
pip install pandas
pip install fastapi
```
## Run
```
uvicorn main:app --reload
```
## GET
```
$ localhost:8000/channel_id?id=video_id&word=anytext
```

You can check usage on localhost:8000/docs