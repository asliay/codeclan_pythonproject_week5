from flask import Flask, render_template

from controllers.albums_controller import albums_blueprint
from controllers.artists_controller import artists_blueprint
from controllers.labels_controller import labels_blueprint
from controllers.genres_controller import genres_blueprint

import repositories.album_repository as album_repository

app = Flask(__name__)

app.register_blueprint(albums_blueprint)
app.register_blueprint(artists_blueprint)
app.register_blueprint(labels_blueprint)
app.register_blueprint(genres_blueprint)

@app.route('/')
def home():
    albums = album_repository.bestsellers()
    return render_template('index.html', albums = albums)


if __name__ == '__main__':
    app.run(debug=True)