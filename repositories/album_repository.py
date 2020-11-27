from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository

# SAVE
def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre, price, cost_price, release_year, label_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [album.title, album.artist.id, album.genre, album.price, album.cost_price, album.release_year, album.label.id]
    results = run_sql(sql, values)
    album.id = results[0]['id']
    return album


# SELECT_ALL
def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        label = label_repository.select(row['label_id'])
        album = Album(row['title'], artist, row['genre'], row['price'], row['cost_price'], row['release_year'], label, row['id'])
        albums.append(album)
    return albums

# SELECT by id

# DELETE ALL
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# DELETE by id
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE