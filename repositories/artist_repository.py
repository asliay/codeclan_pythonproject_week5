from db.run_sql import run_sql

from models.artist import Artist

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



# UPDATE