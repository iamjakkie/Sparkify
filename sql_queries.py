# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS
songplays(songplay_id int PRIMARY KEY, start_time timestamp NOT NULL, user_id int NOT NULL REFERENCES users(user_id), level varchar, song_id varchar NOT NULL REFERENCES songs(song_id), artist_id varchar NOT NULL REFERENCES artists(artist_id), session_id int, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS
users(user_id int PRIMARY KEY, first_name varchar NOT NULL, last_name varchar NOT NULL, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS
songs(song_id varchar PRIMARY KEY, title varchar NOT NULL , artist_id varchar NOT NULL, year int, duration float NOT NULL)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS
artists(artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude float, longitude float)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS
time(start_time timestamp PRIMARY KEY, hour int, day varchar, week int, month varchar, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) DO UPDATE
SET start_time = EXCLUDED.start_time, user_id = EXCLUDED.user_id, level = EXCLUDED.user_id, song_id = EXCLUDED.song_id, artist_id = EXCLUDED.artist_id, session_id = EXCLUDED.session_id, location = EXCLUDED.location, user_agent = EXCLUDED.user_agent;
""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE
SET first_name = EXCLUDED.first_name, last_name = EXCLUDED.last_name, gender = EXCLUDED.gender, level = EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE
SET title = EXCLUDED.title, artist_id = EXCLUDED.artist_id, year = EXCLUDED.year, duration = EXCLUDED.duration
;
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT(artist_id) DO UPDATE
SET name = EXCLUDED.name, location = EXCLUDED.location, latitude = CAST(EXCLUDED.latitude AS FLOAT), longitude = CAST(EXCLUDED.longitude AS FLOAT)
""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(start_time)
DO NOTHING
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, s.artist_id
FROM songs s
JOIN artists a
ON(s.artist_id = a.artist_id)
WHERE s.title=cast(%s as varchar) AND a.name=cast(%s as varchar) AND s.duration=%s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


#test Queries
test_songs = ("""
SELECT COUNT(*) FROM songs
""")
test_users = ("""
SELECT COUNT(*) FROM users
""")
test_artists = ("""
SELECT COUNT(*) FROM artists
""")
test_time = ("""
SELECT COUNT(*) FROM time
""")
test_songplays = ("""
SELECT COUNT(*) FROM songplays
""")

test_table_queries = [test_songs, test_users, test_artists, test_time, test_songplays]
