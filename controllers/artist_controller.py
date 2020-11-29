from flask import Flask, Blueprint, render_template
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
# import repositories.label_repository as label_repository

artists_blueprint = Blueprint("artists", __name__)


# Artists page showing list of Artists in stock
@artists_blueprint.route("/artists")
def artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", artists = artists)
    

# Albums by a specific Artist
@artists_blueprint.route("/artists/<id>")
def artist_albums(id):
    artist = artist_repository.select(id)
    artists_albums = artist_repository.albums_by_artist(artist)
    return render_template ("/artists/show.html", artist = artist, albums = artists_albums)