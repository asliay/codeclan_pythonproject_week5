from flask import Flask, Blueprint, render_template, redirect, request
from models.album import Album
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

# Stock inventory page
@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)


# Delete's stock record and redirects to stock page
@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect("/albums")

# Order Stock?
@albums_blueprint.route("/albums/<id>/order", methods=['POST'])
def order(id):
    #take order amount and update stock amount after pressing button
    # album = album_repository.select(id)
    # album.stock = request.form['order_amount']
    # updated_stock = Album(album.title, album.artist, album.genre, album.price, album.cost_price, album.release_year, album.label, album.stock)
    # album_repository.update(updated_stock)
    # return redirect("/albums")
    pass
