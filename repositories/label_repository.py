from db.run_sql import run_sql

from models.label import Label

# SAVE
def save(label):
    sql = "INSERT INTO labels (name) VALUES (%s) RETURNING id"
    values = [label.name]
    results = run_sql(sql, values)
    label.id = results[0]['id']
    return label

# SELECT_ALL
def select_all():
    labels = []
    sql = "SELECT * FROM labels"
    results = run_sql(sql)
    for row in results:
        artist = Label(row['name'], row['id'])
        labels.append(artist)
    return labels
    

# SELECT by id
def select(id):
    label = None
    sql = "SELECT * from labels WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        label = Label(result['name'], result['id'])
    return label


# DELETE ALL
def delete_all():
    sql = "DELETE FROM labels"
    run_sql(sql)



# UPDATE