from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository
import repositories.genre_repository as genre_repository

# SAVE
def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre_id, price, cost_price, release_year, cover_art, stock, label_id, sales_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [album.title, album.artist.id, album.genre.id, album.price, album.cost_price, album.release_year, album.cover_art, album.stock, album.label.id, album.sales_count]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


# SELECT_ALL
def select_all():
    albums = []

    sql = "SELECT * FROM albums ORDER BY artist_id ASC, release_year DESC"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        label = label_repository.select(row['label_id'])
        genre = genre_repository.select(row['genre_id'])
        album = Album(row['title'], artist, genre, row['price'], row['cost_price'], row['release_year'], row['cover_art'], row['stock'], label, row['sales_count'], row['id'])
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
        label = label_repository.select(result['label_id'])
        genre = genre_repository.select(result['genre_id'])
        album = Album(result['title'], artist, genre, result['price'], result['cost_price'], result['release_year'], result['cover_art'], result['stock'], label, result['sales_count'], result['id'])
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
    sql = "UPDATE albums SET (title, artist_id, genre_id, price, cost_price, release_year, cover_art, stock, label_id, sales_count) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.genre.id, album.price, album.cost_price, album.release_year, album.cover_art, album.stock, album.label.id, album.sales_count, album.id]
    run_sql(sql, values)


# Order Stock
def increase_stock(id):
    # function that adds 1 to stock count of a particular album ??
    sql = "UPDATE albums SET stock = stock + 1 WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Sell stock
def decrease_stock(id):
    sql = "UPDATE albums SET stock = stock -1, sales_count = sales_count +1 WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def bestsellers():
    albums = []
    sql = "SELECT * FROM albums ORDER BY sales_count DESC LIMIT 12"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        label = label_repository.select(row['label_id'])
        genre = genre_repository.select(row['genre_id'])
        album = Album(row['title'], artist, genre, row['price'], row['cost_price'], row['release_year'], row['cover_art'], row['stock'], label, row['sales_count'], row['id'])
        albums.append(album)
    return albums
