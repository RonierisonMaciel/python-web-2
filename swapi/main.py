import os

from fastapi import FastAPI
from sqlmodel import Session
from .db import create_db_and_tables, engine, populate_all_table

app = FastAPI()


@app.on_event("startup")
def on_startup():
    if not os.path.exists("database.sqlite"):
        create_db_and_tables()
        with Session(engine) as session:
            populate_all_table(session)
    else:
        create_db_and_tables


@app.get("/")
def root():
    return {"message": "Hello World!"}
