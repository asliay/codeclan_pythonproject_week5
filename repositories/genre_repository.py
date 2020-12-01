from db.run_sql import run_sql

from models.genre import Genre
from models.artist import Artist
from models.label import Label
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository

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
    sql = "SELECT * FROM genres WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        genre = Genre(result['category'], result['id'])
    return genre

def delete_all():
    sql = "DELETE FROM genres"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM genres WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def albums_by_genre(genre):
    albums = []

    sql = "SELECT * FROM albums WHERE genre_id = %s"
    values = [genre.id]
    results = run_sql(sql,values)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        label = label_repository.select(row['label_id'])
        album = Album(row['title'], artist, genre, row['price'], row['cost_price'], row['release_year'], row['cover_art'], row['stock'], label, row['id'])
        albums.append(album)
    return albums
    