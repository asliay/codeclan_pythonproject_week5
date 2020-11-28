from flask import Flask, Blueprint, render_template
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artists_blueprint = Blueprint("artists", __name__)

# Stock inventory page
@artists_blueprint.route("/artists/<id>")
def albums(id):
    album = album_repository.select(id)
    artist = artist_repository.select(id)
    artists_albums = artist_repository.albums_by_artist(artist)
    return render_template ("/artists/show.html", artist = artist, album = album, albums = artists_albums)