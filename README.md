# Prerequisites
- Python 3.6 or higher
- FastAPI
- uvicorn (optional, for running the API in development)
## Step 1: Create a new FastAPI application
First, create a new directory for your project and navigate to it in your terminal. Then, create a new file called app.py and add the following code to it:

```python
from fastapi import FastAPI

app = FastAPI()
```

This code creates a new FastAPI application and assigns it to the app variable.

## Step 2: Add endpoints to the API
Next, we will add some endpoints to the API. An endpoint is a specific URL that can be accessed by making an HTTP request to it. In FastAPI, you can create endpoints by decorating a function with the @app.route() decorator and specifying the route for the endpoint as an argument.

Here is an example of an endpoint that returns a simple "Hello, World" message when accessed:

```python
@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}
```

In this example, the hello_world() function is decorated with @app.route("/"), which means it will be accessible at the / route (i.e., the root URL of the API). The function returns a dictionary containing the "message" key and the value "Hello, World!".

You can add as many endpoints as you like to your API. Here is an example of a few more endpoints:

```python
@app.route("/videos/{channel_id}")
def get_videos(channel_id):
    return {"channel_id": channel_id, "videos": ["video1", "video2", "video3"]}

@app.route("/channels/{channel_id}/videos/{video_id}")
def get_video(channel_id, video_id):
    return {"channel_id": channel_id, "video_id": video_id, "title": "My Video"}

@app.route("/search")
def search(q: str):
    return {"results": [{"title": "Video 1", "url": "/videos/1"}, {"title": "Video 2", "url": "/videos/2"}]}
```

In the first endpoint, we have a route with a parameter channel_id in it (e.g., /videos/123). This means that when the endpoint is accessed, the channel_id value will be passed as an argument to the get_videos() function.

The second endpoint also has two parameters in the route: channel_id and video_id. These will be passed as arguments to the get_video() function when the endpoint is accessed.

The third endpoint has a query parameter q, which can be passed in the URL after a ? character (e.g., /search?q=hello). This parameter is then available as the q argument in the search() function.

## Step 3: Enable CORS (Cross-Origin Resource Sharing)
CORS is a mechanism that allows web applications on different domains to access each other's resources. This is necessary because, by default, web browsers block requests to a resource on a different domain for security reasons.

To enable CORS for your FastAPI application, you need to add the CORSMiddleware provided by FastAPI to your app. This middleware allows you to specify the origins that are allowed to make requests to your API, as well as other options such as the allowed HTTP methods and headers.

Here is an example of how to add the CORSMiddleware to your FastAPI app and allow requests from any origin:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

In this example, we added the CORSMiddleware to the app object using the app.add_middleware() method. We passed in several arguments to the middleware:

- allow_origins: This is a list of origins that are allowed to make requests to the API. We specified ["*"], which means that requests from any origin will be allowed.
allow_credentials: This specifies whether credentials (e.g., cookies) are allowed in requests. We set it to True to allow them.
- allow_methods: This is a list of HTTP methods that are allowed in requests. We specified ["*"], which means that all methods (e.g., GET, POST, PUT, etc.) are allowed.
- allow_headers: This is a list of HTTP headers that are allowed in requests. We specified ["*"], which means that all headers are allowed.

After adding the CORSMiddleware, your FastAPI app will allow requests from any origin and with any method and headers.

You can also specify specific origins, methods, and headers that you want to allow, instead of using the wildcard "*" value. For example:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://www.example.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["X-Custom-Header"],
)
```
In this example, we only allow requests from the http://localhost:3000 and https://www.example.com origins, only allow the GET, POST, and PUT methods, and only allow requests with the X-Custom-Header header.

## Step 4: Run the API
Now that we have our FastAPI application with some endpoints defined, we can run it to start the web server.

To run the server, use the uvicorn command and specify the name of the app.py file as an argument. For example:

```
uvicorn app:app
```
This will start the server and listen for incoming requests on port 8000 by default. You can specify a different port using the --port option. For example, to listen on port 5000, you would use the following command:

```
uvicorn app:app --port 5000
```
Once the server is running, you can access the endpoints of your API by making HTTP requests to them. For example, to access the / endpoint, you can use curl or a web browser to make a GET request to http://localhost:8000/ (replace 8000 with the port number you specified if you used a different one). This should return the JSON object with the "message" key and the value "Hello, World!".

You can also access the other endpoints by appending the route to the base URL. For example, to access the /videos/{channel_id} endpoint, you would make a GET request to http://localhost:8000/videos/123 (replace 123 with the actual channel_id you want to use).

Try making requests to the different endpoints of your API and see the results they return.

## Conclusion
In this tutorial, we learned how to create a web API using FastAPI and enable CORS with my sample. We also learned how to add endpoints to the API and run the server to start listening for requests.

FastAPI is a powerful framework for building web APIs, and it offers many advanced features for building scalable and efficient APIs. To learn more about FastAPI, check out the [official documentation](https://fastapi.tiangolo.com/)
