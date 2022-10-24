from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()

def test_get_all_movies():

    movie_repository.create_movie('Star Wars IV', 'George Lucas', 5)
    movie_repository.create_movie('Star Wars V', 'George_Lucas', 4)
    movie_repository.create_movie('Star Wars VI', 'GeorgeLucas', 4.5)

    movieIV = Movie('Star Wars IV', 'George Lucas', 5)
    movieV = Movie('Star Wars V', 'George_Lucas', 4)
    movieVI = Movie('Star Wars VI', 'GeorgeLucas', 4.5)

    assert movie_repository.get_all_movies()[0].title == movieIV.title
    assert movie_repository.get_all_movies()[1].director == movieV.director
    assert movie_repository.get_all_movies()[2].rating == movieVI.rating

    movie_repository._db.clear()

