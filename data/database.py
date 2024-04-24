import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('../users.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            bio TEXT
        )
        """)
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS word_filter(
                        server_id INTEGER,
                        word TEXT,
                        FOREIGN KEY(server_id) REFERENCES users(id)
                    )
                """)
        self.connection.commit()

    def add_word_to_filter(self, server_id, word):
        self.cursor.execute("INSERT INTO word_filter(server_id, word) VALUES(?, ?)", (server_id, word.lower()))
        self.connection.commit()

    def get_filtered_words(self, server_id):
        self.cursor.execute("SELECT word FROM word_filter WHERE server_id=?", (server_id,))
        return self.cursor.fetchall()

    def remove_word_from_filter(self, server_id, word):
        self.cursor.execute('DELETE FROM word_filter WHERE server_id = ? AND word = ?', (server_id, word))
        self.connection.commit()

    def get_bio(self, user_id):
        self.cursor.execute("SELECT bio FROM users WHERE user_id=?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def set_bio(self, user_id, bio):
        self.cursor.execute("INSERT OR REPLACE INTO users (user_id, bio) VALUES (?, ?)", (user_id, bio))
        self.connection.commit()


database = Database()