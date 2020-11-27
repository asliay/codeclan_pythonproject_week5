from flask import Flask, Blueprint, render_template
from models.album import Album
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)