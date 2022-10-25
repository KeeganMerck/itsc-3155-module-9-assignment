from flask import Flask, redirect, render_template

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, movies = movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    movie-title = request.form.git('title', type=str)
    movie-director = request.form.git('director', type=str)
    movie-rating = request.form.git('rating', type=int)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():    
    # TODO: Feature 3
    movie_title = request.args.get('movie-title', type=str)
    if movie_title: 
        yes = True
    else:
        yes = False
    return render_template('search_movies.html', search_active=True, movie = movie_repository.get_movie_by_title(movie_title), entered = yes)

