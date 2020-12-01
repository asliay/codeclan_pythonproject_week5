from flask import Flask, Blueprint, render_template, request, redirect
from models.label import Label
import repositories.label_repository as label_repository
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

labels_blueprint = Blueprint("labels", __name__)

@labels_blueprint.route("/labels")
def labels():
    labels = label_repository.select_all()
    return render_template("labels/index.html", labels = labels)

# NEW
# GET ("/labels/new")
@labels_blueprint.route("/labels/new", methods=['GET'])
def new_label():
    return render_template("labels/new.html")

# CREATE
# POST "/labels"
@labels_blueprint.route("/labels", methods=['POST'])
def create_label():
    name = request.form['label-name']
    label = Label(name)
    label_repository.save(label)
    return redirect("/labels")

# Show albums by labels
@labels_blueprint.route("/labels/<id>")
def label_albums(id):
    label = label_repository.select(id)
    labels_albums = label_repository.albums_by_label(label)
    return render_template("labels/show.html", label = label, albums = labels_albums)
    