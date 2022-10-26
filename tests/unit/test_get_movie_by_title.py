from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()

def test_get_movie_by_title():
    movie_repository.create_movie('Minions', 'Gru', 5)
    movie_repository.create_movie('Star Wars V', 'George Lucas', 3)
    movie_repository.create_movie('Harry Potter', 'J.K Rowling', 4)

    assert type(movie_repository.get_movie_by_title('Star Wars V')) == Movie
    assert type(movie_repository.get_movie_by_title('Minions')) == Movie
    assert movie_repository.get_movie_by_title('Transformers') == None

    movie_repository._db.clear()
