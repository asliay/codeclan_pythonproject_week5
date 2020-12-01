from db.run_sql import run_sql

from models.artist import Artist
from models.label import Label
from models.album import Album

# SAVE 
def save(genre):
    sql = "INSERT INTO genres (category) VALUES (%s) RETURNING id"
    values = [genre.category]
    results = run_sql(sql, values)
    genre.id = results[0]['id']
    return genre
