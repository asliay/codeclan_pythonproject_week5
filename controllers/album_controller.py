from flask import Flask, Blueprint, render_template, redirect, request
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

albums_blueprint = Blueprint("albums", __name__)

# Stock inventory page
@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)

# NEW
#GET "/albums/new"
@albums_blueprint.route("/albums/new", methods=['GET'])
def new_album():
    artists = artist_repository.select_all()
    return render_template("albums/new.html", artists = artists)

# CREATE
# POST "/albums"
@albums_blueprint.route("/albums", methods=['POST'])
def create_album():
    title = request.form['title']
    artist_id = request.form['artist_id']
    artist = artist_repository.select(artist_id)
    genre = request.form['genre']
    price = request.form['price']
    cost_price = request.form['cost-price']
    release_year = request.form['release-year']
    label = request.form['record-label']
    stock = request.form['stock']
    album = Album(title, artist, genre, price, cost_price, release_year, stock, label)
    album_repository.save(album)
    return redirect("/albums")


# SHOW
# GET "/albums/<id>"
@albums_blueprint.route("/albums/<id>", methods=['GET'])
def show_album(id):
    album = album_repository.select(id)
    return render_template("albums/show.html", album = album)


# EDIT
# GET "/albums/<id>/edit"



# UPDATE
# PUT "albums/<id>"



# Delete's stock record and redirects to stock page
@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect("/albums")

# Order Stock?
@albums_blueprint.route("/albums/<id>/order", methods=['POST'])
def update_stock(id):
    pass