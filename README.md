# Python Weather App

A Weather App made with Python, Flask, and deployed using Heroku

## Requirements

- Python
- Code editor of your choice
- Virtual environment (optional)
- Docker
- Heroku CLI

### Helpful Commands

Create virtual environment:
`python -m venv env`

Enter virtual environment:
`source ./env/Scripts/activate`

Install dependencies
`pip install flask requests python-dotenv`

Run flask server
`flask run`

### To start Heroku Container Deployment

`docker login`

`docker build . -t app`

`docker image ls`

`docker run -p 5000:5000 --env-file .env app`

`heroku login` (to logout, `heroku logout`)

`heroku create my-great-weather` (if name is taken, choose another)

`heroku stack:set container --app my-great-weather`

`heroku config:set FLASK_APP=server --app my-great-weather`

`heroku config:set FLASK_ENV=production --app my-great-weather` (set environment variables)
