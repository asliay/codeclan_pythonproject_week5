from flask import Flask, Blueprint, render_template, redirect, request
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository

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
    labels = label_repository.select_all()
    return render_template("albums/new.html", artists = artists, labels = labels)

# CREATE
# POST "/albums"
@albums_blueprint.route("/albums", methods=['POST'])
def create_album():
    title = request.form['title']
    artist = artist_repository.select(request.form['artist_id'])
    genre = request.form['genre']
    price = request.form['price']
    cost_price = request.form['cost-price']
    release_year = request.form['release-year']
    cover_art = request.form['cover_art']
    stock = request.form['stock']
    label = label_repository.select(request.form['label_id'])
    album = Album(title, artist, genre, price, cost_price, release_year, cover_art, stock, label)
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
@albums_blueprint.route("/albums/<id>/edit", methods=['GET'])
def edit_album(id):
    album = album_repository.select(id)
    artists = artist_repository.select_all()
    labels = label_repository.select_all()
    return render_template("albums/edit.html", album = album, artists = artists, labels = labels)


# UPDATE - 
# PUT "albums/<id>"
@albums_blueprint.route("/albums/<id>", methods=['POST'])
def update_album(id):
    title = request.form['title']
    artist = artist_repository.select(request.form['artist_id'])
    genre = request.form['genre']
    price = request.form['price']
    cost_price = request.form['cost-price']
    release_year = request.form['release-year']
    cover_art = request.form['cover_art']
    stock = request.form['stock']
    label = label_repository.select(request.form['label_id'])
    album = Album(title, artist, genre, price, cost_price, release_year, cover_art, stock, label, id)
    album_repository.update(album)
    return redirect("/albums")


# Delete's stock record and redirects to stock page
@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect("/albums")
