from flask import Flask, render_template

from controllers.album_controller import albums_blueprint
from controllers.artist_controller import artists_blueprint
from controllers.label_controller import labels_blueprint
from controller.genre_controller import genres_blueprint

app = Flask(__name__)

app.register_blueprint(albums_blueprint)
app.register_blueprint(artists_blueprint)
app.register_blueprint(labels_blueprint)
app.register_blueprint(genres_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)