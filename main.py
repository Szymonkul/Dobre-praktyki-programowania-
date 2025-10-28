from fastapi import FastAPI

from fastapi import FastAPI

from functionals import Movies, Raitings, Links, get_csv_data

app = FastAPI()


@app.get("/")
async def root():
    return get_csv_data("movies.csv", Movies)


@app.get("/movies/")
async def get_movies():
    return get_csv_data("movies.csv", Movies)


@app.get("/raitings/")
async def get_raitings():
    return get_csv_data("raitings.csv", Raitings)


@app.get("/tags/")
async def get_tags():
    return {'aka': '12'}  # get_csv_data("tags.csv", Tags)


@app.get("/links")
async def get_links():
    return [obj.__dict__ for obj in get_csv_data("links.csv", Links)]
