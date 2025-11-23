from fastapi import FastAPI, Request
from dotenv import load_dotenv
from pathlib import Path
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from fastapi.responses import JSONResponse

def create_app(env_file_path:str | Path):
    load_dotenv(dotenv_path=env_file_path)
    app = FastAPI()
    return app