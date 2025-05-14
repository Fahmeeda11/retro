import sqlite3
#connecting with db
db_connect = sqlite3.connect('retroboard.db')
# create table for cards data
db_connect.execute('''
    CREATE TABLE IF NOT EXISTS cards (
        id TEXT PRIMARY KEY,
        type TEXT,
        text TEXT
    )
''')
#create table for comments data
db_connect.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id TEXT,
        text TEXT,
        FOREIGN KEY(card_id) REFERENCES cards(id)
    )
''')
#commit the changes of db
db_connect.commit()
#close the db
db_connect.close()