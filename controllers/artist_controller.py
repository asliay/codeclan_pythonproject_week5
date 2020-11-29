from flask import Flask, Blueprint, render_template
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import repositories.label_repository as label_repository

artists_blueprint = Blueprint("artists", __name__)


# Artists page
@artists_blueprint.route("/artists")
def artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", artists = artists)
    

# Albums by artist
@artists_blueprint.route("/artists/<id>")
def artist_albums(id):
    album = album_repository.select(id)
    #Need to figure out how to get correct label showing up?
    artist = artist_repository.select(id)
    artists_albums = artist_repository.albums_by_artist(artist)
    return render_template ("/artists/show.html", artist = artist, album = album, albums = artists_albums)