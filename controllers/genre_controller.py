from flask import Flask, Blueprint, render_template
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