from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository
# import repositories.label_repository as label_repository

# SAVE
def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre, price, cost_price, release_year, stock, label) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [album.title, album.artist.id, album.genre, album.price, album.cost_price, album.release_year, album.stock, album.label]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


# SELECT_ALL
def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        
        album = Album(row['title'], artist, row['genre'], row['price'], row['cost_price'], row['release_year'], row['stock'], row['label'], row['id'])
        albums.append(album)
    return albums

# SELECT by id
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'], result['price'], result['cost_price'], result['release_year'], result['label'], result['id'])
    return album


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
def update(album):
    sql = "UPDATE albums SET (title, artist_id, genre, price, cost_price, release_year, stock, label) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.genre, album.price, album.cost_price, album.release_year, album.stock, album.label]
    run_sql(sql, values)


