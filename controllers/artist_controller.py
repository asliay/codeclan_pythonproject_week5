from flask import Flask, Blueprint, render_template
from models.artist import Artist
import repositories.artist_repository as artist_repository

artists_blueprint = Blueprint("artists", __name__)