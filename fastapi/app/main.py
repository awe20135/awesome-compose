from fastapi import FastAPI
from pathlib import Path
from os import environ

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK!"}

@app.get("/password")
def get_password():
    password_file = environ.get("PASSWORD_FILE")
    secret_path = Path(password_file)
    password = secret_path.read_text().strip() if secret_path.exists() else None
    return { "password": password }

@app.get("/token")
def get_token():
    token_file = environ.get("TOKEN_FILE")
    secret_path = Path(token_file)
    token = secret_path.read_text().strip() if secret_path.exists() else None
    return { "token": token }