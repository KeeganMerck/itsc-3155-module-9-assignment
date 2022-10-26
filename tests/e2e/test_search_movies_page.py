from urllib import response

from flask import request
from app import app
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository()

def test_search_movies_page():
    test_app = app.test_client()
    response = test_app.get('/movies/search')

    
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data
    assert b'<p class="mb-3">Search for a movie rating below</p>' in response.data
    assert b'<button class="btn btn-outline-success" type="submit">Search</button>' in response.data


    movie_repository.create_movie('Star Wars V', 'George Lucas', 3)
    response = test_app.get('/movies/search?movie-title=Star+Wars+V')
    
    assert b'<td>Star Wars V</td>' in response.data
    assert b'<td>George Lucas</td>' in response.data
    assert b'<td>3</td>' in response.data
    assert b'<td>Minions</td>' not in response.data
