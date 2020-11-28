from flask import Flask, Blueprint, render_template, redirect, request
from models.album import Album
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

# Stock inventory page
@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)

# Show all artists albums 
@albums_blueprint.route("/albums/<id>")


# Delete's stock record and redirects to stock page
@albums_blueprint.route("/albums/<id>/delete", methods=['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect("/albums")

# Order Stock?
@albums_blueprint.route("/albums/<id>/order", methods=['POST'])
def update_stock(id):
    pass