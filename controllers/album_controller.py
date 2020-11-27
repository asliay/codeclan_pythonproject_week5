from flask import Flask, Blueprint, render_template
from models.album import Album
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)
    