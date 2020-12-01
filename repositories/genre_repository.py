from db.run_sql import run_sql

from models.genre import Genre
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

def select_all():
    genres = []
    sql = "SELECT * FROM genres ORDER BY category"
    results = run_sql(sql)
    for row in results:
        genre = Genre(row['category'], row['id'])
        genres.append(genre)
    return genres

def select(id):
    genre = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        genre = Genre(result['category'], result['id'])
    return genre