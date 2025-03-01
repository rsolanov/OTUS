## Running with Docker

To run the application in a Docker container, use the following command:

```
docker build -t fastapi_app . 
docker run -d -p 8000:8000 --name fastapi_app fastapi_app
```
After running the command, the application will be available at http://127.0.0.1:8000/ping/.