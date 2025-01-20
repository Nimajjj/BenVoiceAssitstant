import sqlite3

class DBController:
    def __init__(self, db_name="ben.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def write(self, text):
        self.cursor.execute("INSERT INTO voice_request_history (request_content) VALUES (?)", (text,))
        self.conn.commit()

    def read(self):
        self.cursor.execute("SELECT request_content FROM voice_request_history ORDER BY id DESC LIMIT 10")
        result = self.cursor.fetchall()
        return result if result else None

    def close(self):
        self.conn.close()
