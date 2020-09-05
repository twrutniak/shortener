# shortener
URL shortener created with Python's Flask web framework, containerized and integrated with Nginx as well as Mongodb.

## How to use
In order to use this app, you can either run it using included Virtual Environment or run it with Docker (recommended). 
This app requires a couple of environmental variables to be set, explained in the next section.
If using Docker, any changes to html files themselves should be followed with building a new image as .html are served via reverse proxying Nginx. It is not the case with /static directory, which can be ammended at any given time, followed by Nginx restart.

Assuming Mongodb is listening on port 21707 (required to succesful start):
##### venv
```
source venv/bin/activate
gunicorn -b :8000 app:app
```
It will run on gunicorn's default port 8000.
##### docker container run
```
docker container run --name shortener --rm -p 80:8000 twrutniak/shortener:1.0
```
There's also docker-compose.yml file provided that sets everything up automatically.
```
docker-compose up
```
Remember docker-compose is not a production tool, in that case it should be ran in Swarm mode.
## Envirionmental variables
These variables can be set either in Dockerfile, docker-compose.yml, virtual environment or directly in host's variables.
- **MONGO_HOST** mongo host, **required**.
- **MONGO_PORT** mongo port, **required**.
- **TOKEN_NBYTES** number of bytes constituting URL token, on average each byte results in approximately 1.3 characters. Default value is 4.
- **ADS** signify whether you want to include ads or not, can be set to whatever value. It is not set by default. If set, app will render ads.html with timeout passed instead of instantly redirecting user.
- **ADS_REDIRECT_TIMEOUT** timeout passed to ads.html, works only if **ADS** is set. In combination with javascript it is used to redirect user to target adress after set time runs out, it is set to 5 by default.
