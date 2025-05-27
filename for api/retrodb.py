import sqlite3
#connecting with db
db_connect = sqlite3.connect('retroboard.db')
#create tablee for single board data
db_connect.execute('''
    CREATE TABLE IF NOT EXISTS boards(
        board_id INTEGER PRIMARY KEY AUTOINCREMENT,
        board_name VARCHAR(255) NOT NULL,
        description TEXT           
    )
''')

# create table for cards data
db_connect.execute('''
    CREATE TABLE IF NOT EXISTS cards (
        card_id INTEGER PRIMARY KEY AUTOINCREMENT,
        board_id INT NOT NULL,
        section_type TEXT CHECK(section_type IN ('Went Well', 'To Improve', 'Action Items')) NOT NULL,
        card_text TEXT NOT NULL,
        FOREIGN KEY (board_id) REFERENCES boards(board_id) ON DELETE CASCADE
    )
''')

#create table for comments data
db_connect.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INT NOT NULL,
        comment_text TEXT NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards(card_id) ON DELETE CASCADE
    )
''')
#commit the changes of db
db_connect.commit()
#close the db
db_connect.close()


