# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal, engine
import functionality
from models import Movie, Rating, Tag, Link, Base

app = FastAPI()
db = SessionLocal()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    functionality.load_movies()
    functionality.load_tags()
    functionality.load_ratings()
    functionality.load_links()
    print("Dane załadowane do bazy (albo pominięto, jeśli już były)")


@app.get("/")
async def root():
    return {"Hello": "World"}

def row_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@app.get("/movies")
def get_movies():
    rows = db.query(Movie).all()
    return [row_to_dict(r) for r in rows]

@app.get("/ratings")
def get_ratings():
    rows = db.query(Rating).all()
    return [row_to_dict(r) for r in rows]

@app.get("/tags")
def get_tags():
    rows = db.query(Tag).all()
    return [row_to_dict(r) for r in rows]

@app.get("/links")
def get_links():
    rows = db.query(Link).all()
    return [row_to_dict(r) for r in rows]
