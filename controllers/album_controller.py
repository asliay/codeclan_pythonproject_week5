from flask import Flask, Blueprint, render_template, redirect, request
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository
import repositories.genre_repository as genre_repository

albums_blueprint = Blueprint("albums", __name__)

# Stock inventory page
@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)


# Enter stock information for a new album
@albums_blueprint.route("/albums/new", methods=['GET'])
def new_album():
    artists = artist_repository.select_all()
    labels = label_repository.select_all()
    genres = genre_repository.select_all()
    return render_template("albums/new.html", artists = artists, labels = labels, genres = genres)

# CREATE
# Add new album to stock catalogue
@albums_blueprint.route("/albums", methods=['POST'])
def create_album():
    title = request.form['title']
    artist = artist_repository.select(request.form['artist_id'])
    genre = request.form['genre']
    price = request.form['price']
    cost_price = request.form['cost-price']
    release_year = request.form['release-year']
    cover_art = request.form['cover-art']
    stock = request.form['stock']
    label = label_repository.select(request.form['label_id'])
    album = Album(title, artist, genre, price, cost_price, release_year, cover_art, stock, label)
    album_repository.save(album)
    return redirect("/albums")


# SHOW
# GET "/albums/<id>"
# Shows a specific album entry
@albums_blueprint.route("/albums/<id>", methods=['GET'])
def show_album(id):
    album = album_repository.select(id)
    return render_template("albums/show.html", album = album)


# EDIT
# GET "/albums/<id>/edit"
# Edit information about an album
@albums_blueprint.route("/albums/<id>/edit", methods=['GET'])
def edit_album(id):
    album = album_repository.select(id)
    artists = artist_repository.select_all()
    genres = genre_repository.select_all()
    labels = label_repository.select_all()
    return render_template("albums/edit.html", album = album, artists = artists, genres = genres, labels = labels)


# UPDATE - 
# PUT "albums/<id>"
# Save changes to album
@albums_blueprint.route("/albums/<id>/updated", methods=['POST'])
def update_album(id):
    title = request.form['title']
    artist = artist_repository.select(request.form['artist_id'])
    genre = genre_repository.select(request.form['genre_id'])
    price = float(request.form['price'])
    cost_price = float(request.form['cost-price'])
    release_year = request.form['release-year']
    cover_art = request.form['cover-art']
    stock = int(request.form['stock'])
    label = label_repository.select(request.form['label_id'])
    album = Album(title, artist, genre, price, cost_price, release_year, cover_art, stock, label, id)
    album_repository.update(album)
    return render_template("/albums/updated.html", **locals())


# Delete's stock record and redirects to stock page
@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect("/albums")

# 'Orders' stock (+1 to stock count) on specific album and redirects to show album page
@albums_blueprint.route("/albums/<id>/order", methods=['POST'])
def order_stock(id):
    album_repository.increase_stock(id)
    return redirect(f"/albums/{id}")

# 'Sell's stock (-1 to stock count) on specific album and redirects to show album page
@albums_blueprint.route("/albums/<id>/sell", methods=['POST'])
def sell_stock(id):
    album = album_repository.select(id)
    if album.stock > 0:
        album_repository.decrease_stock(id)
    return redirect(f"/albums/{id}")