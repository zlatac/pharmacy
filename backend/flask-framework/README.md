# Flask framework

This project was made with python version 3.x

## Install

- git pull this project
- cd to the project directory
- create a python [virtual environment](https://flask.palletsprojects.com/en/stable/installation/#virtual-environments)
- activate the python [virtual environment](https://flask.palletsprojects.com/en/stable/installation/#activate-the-environment)
- run `pip install -r requirements.txt`

## Development server

To start a local development server, run:

```bash
flask run
```

## Frontend local server integration
All frontend apps in this directory will by default be looking for a backend service at `http://localhost:8000`

use these environment variables
```
FLASK_APP=app
FLASK_RUN_PORT=8000
FLASK_ENV=development
```