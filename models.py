# models.py
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movieId = Column(Integer, index=True)
    title = Column(Text)
    genres = Column(Text)

class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movieId = Column(Integer, index=True)
    imdbId = Column(String)
    tmdbId = Column(String)

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer,  index=True)
    movieId = Column(Integer, index=True)
    rating = Column(Float)
    timestamp = Column(Integer)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, index=True)
    movieId = Column(Integer, index=True)
    tag = Column(Text)
    timestamp = Column(Integer)