from flask import Flask, Blueprint, render_template, request, redirect
from models.genre import Genre
import repositories.genre_repository as genre_repository

genres_blueprint = Blueprint("genres", __name__)

# Genres view showing list of genres
@genres_blueprint.route("/genres")
def genres():
    genres = genre_repository.select_all()
    return render_template("genres/index.html", genres = genres)

# Form to add a new Genre to Database
@genres_blueprint.route("/genres/new", methods=['GET'])
def new_genre():
    return render_template("genres/new.html")

# Creates new Genre and updates Genre list
@genres_blueprint.route("/genres", methods=['POST'])
def create_genre():
    category = request.form['genre-category']
    genre = Genre(category)
    genre_repository.save(genre)
    return redirect("/genres")

# Albums of a specific genre
@genres_blueprint.route("/genres/<id>")
def genre_albums(id):
    genre = genre_repository.select(id)
    genres_albums = genre_repository.albums_by_genre(genre)
    return render_template("genres/show.html", genre = genre, albums = genres_albums)