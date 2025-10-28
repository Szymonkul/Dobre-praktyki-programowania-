from fastapi import FastAPI

from fastapi import FastAPI

from functionals import Movies, Raitings, Links, get_csv_data, Tags

app = FastAPI()


@app.get("/")
async def root():
    return {'Hello' : 'World'}


@app.get("/movies/")
async def get_movies():
    return get_csv_data("movies.csv", Movies)


@app.get("/raitings/")
async def get_raitings():
    return get_csv_data("raitings.csv", Raitings)


@app.get("/tags/")
async def get_tags():
    return get_csv_data("tags.csv", Tags)


@app.get("/links/")
async def get_links():
    return get_csv_data("links.csv", Links)
