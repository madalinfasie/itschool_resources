import sqlite3

cleanup_query = 'DROP TABLE IF EXISTS utilizatori'
create_users_query = '''CREATE TABLE utilizatori (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT,
    nr_animale INTEGER
)'''

insert_users_query = '''INSERT INTO utilizatori
        VALUES (?, ?, ?, ?)'''

test_query = 'SELECT * FROM utilizatori'

users = (
    (1, 'mfasie', 'mfasie@gmail.com', 5),
    (2, 'paco', 'paco@ste.com', 1),
    (3, 'ionionel', 'iontiriac@gmail.com', 3),
    (4, 'mariaa', 'maria.lu.ion@gmail.com', 2)
)

con = sqlite3.connect('test.db')
with con:
    con.execute(cleanup_query)
    con.execute(create_users_query)
    con.executemany(insert_users_query, users)

    stored_users = con.execute(test_query)

print('Database is now up to date')
print('Utilizatori', stored_users.fetchall())


