# from flask import Flask, Blueprint, render_template
# from models.label import Label
# import repositories.label_repository as label_repository
# import repositories.artist_repository as artist_repository
# import repositories.album_repository as album_repository

# labels_blueprint = Blueprint("labels", __name__)

# @labels_blueprint.route("/labels")
# def labels():
#     labels = label_repository.select_all()
#     return render_template("labels/index.html", labels = labels)


# # Show albums by labels
# @labels_blueprint.route("/labels/<id>")
# def label_albums(id):
#     # album = album_repository.select(id)
#     # label = label_repository.select(id)
#     # # artist = artist_repository.select(id)  incorrect artist showing up
#     # label_albums = label_repository.albums_by_label(label)
#     # return render_template("labels/show.html", album = album, label = label, albums = label_albums)
#     pass