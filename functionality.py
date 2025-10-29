from pathlib import Path
import csv
from db import SessionLocal, engine
from models import Base, Movie, Rating, Tag, Link

CSV_DIR = Path("csv")

def get_csv_data(filepath, elements_count: int):
    with open(filepath, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)
        return [row[:elements_count] for row in reader]

def table_count(model):
    session = SessionLocal()
    try:
        return session.query(model).count()
    finally:
        session.close()

def load_movies():
    rows = get_csv_data(CSV_DIR / "movies.csv", 3)
    objs = []
    for r in rows:
        objs.append(Movie(
            movieId = int(r[0]) if r[0] not in (None, "") else None,
            title = r[1],
            genres = r[2]
        ))
    session = SessionLocal()
    try:
        session.bulk_save_objects(objs)
        session.commit()
    finally:
        session.close()

def load_tags():
    rows = get_csv_data(CSV_DIR / "tags.csv", 4)
    objs = []
    for r in rows:
        objs.append(Tag(
            userId = int(r[0]) if r[0] not in (None, "") else None,
            movieId = int(r[1]) if r[1] not in (None, "") else None,
            tag = r[2],
            timestamp = int(r[3]) if r[3] not in (None, "") else None
        ))
    session = SessionLocal()
    try:
        session.bulk_save_objects(objs)
        session.commit()
    finally:
        session.close()

def load_ratings():
    rows = get_csv_data(CSV_DIR / "ratings.csv", 4)
    objs = []
    for r in rows:
        objs.append(Rating(
            userId = int(r[0]) if r[0] not in (None, "") else None,
            movieId = int(r[1]) if r[1] not in (None, "") else None,
            rating = float(r[2]) if r[2] not in (None, "") else None,
            timestamp = int(r[3]) if r[3] not in (None, "") else None
        ))
    session = SessionLocal()
    try:
        session.bulk_save_objects(objs)
        session.commit()
    finally:
        session.close()

def load_links():
    rows = get_csv_data(CSV_DIR / "links.csv", 3)
    objs = []
    for r in rows:
        objs.append(Link(
            movieId = int(r[0]) if r[0] not in (None, "") else None,
            imdbId = r[1],
            tmdbId = r[2]
        ))
    session = SessionLocal()
    try:
        session.bulk_save_objects(objs)
        session.commit()
    finally:
        session.close()


