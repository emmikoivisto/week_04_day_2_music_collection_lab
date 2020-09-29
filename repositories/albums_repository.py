from db.run_sql import run_sql 

from models.albums import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id)"
    values = [album.title, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album
    

def list_all():
    albums = []

    sql = "SELECT * from albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['genre'], row['artist_id'])
        albums.append(album)
    return albums


