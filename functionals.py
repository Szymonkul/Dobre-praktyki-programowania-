import csv


class Movies:
    columns = 3

    def __init__(self, title, categories, movie_id):
        self.movie_id = movie_id
        self.title = title
        self.categories = categories

    def __str__(self):
        return f"id: {self.movie_id} title: {self.title}\ncategories: {self.categories} "


class Links:
    columns = 3

    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movieId = movie_id
        self.imdbId = imdb_id
        self.tmdbId = tmdb_id

    def __str__(self):
        return f"id: {self.movieId} imdbId: {self.imdbId}\ntmdbId: {self.tmdbId} "


class Raitings:
    columns = 4

    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

    def __str__(self):
        return f"userid: {self.userId}\nmovieid: {self.movieId}\nrating: {self.rating}\ntimestamp: {self.timestamp}"


class Tags:
    columns = 4

    def __init__(self,userId,movieId,tag,timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

    def __str__(self):
        return f"UserId: {self.userId}\nMovieId: {self.movieId}\nTag: {self.tag} timestamp: {self.timestamp}"

def get_csv_data(filename, model):
    with open(filename,encoding="utf-8") as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            result.append(model(*row[:model.columns]).__dict__)
        return result

