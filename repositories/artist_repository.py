from db.run_sql import run_sql

from models.artist import Artist
# from models.label import Label
from models.album import Album

# SAVE
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist

# SELECT_ALL
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists


# SELECT by id
def select(id):
    artist = None
    sql = "SELECT * from artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist


# DELETE ALL
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# DELETE by id
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# UPDATE
def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name]
    run_sql(sql, values)


# Shows all albums by a specific artist
def albums_by_artist(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['artist_id'], row['genre'], row['price'], row['cost_price'], row['release_year'], row['stock'], row['label'], row['id'])
        albums.append(album)
    return albums