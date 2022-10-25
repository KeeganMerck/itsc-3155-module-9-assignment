from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()

def test_create_movie():

    movie_repository.create_movie('Star Wars IV', 'George Lucas', 5)

    movieIV = Movie('Star Wars IV', 'George Lucas', 5)

    assert movie_repository.get_all_movies()[0].title == movieIV.title

    movie_repository._db.clear()