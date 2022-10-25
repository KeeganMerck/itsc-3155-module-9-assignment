from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()


def test_all_movies_page():
    test_app = app.test_client()
    response = test_app.get('/movies')

    assert b'<td>No Movies to Display</td>' in response.data

    movie_repository.create_movie('Star Wars IV', 'George Lucas', 5)

    response = test_app.get('/movies')

    assert b'<td>Star Wars IV</td>' in response.data

    movie_repository._db.clear()
