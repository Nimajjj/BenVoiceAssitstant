import sqlite3

class DBController:
    def __init__(self, db_name="/Users/pat/workspace/BenVoiceAssitstant/ben_back/DBController/ben.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def write(self, text, answer):
        self.cursor.execute(
            "INSERT INTO voice_request_history (voice_request, voice_answer) VALUES (?, ?)", (text, answer))
        self.conn.commit()

    def read(self):
        self.cursor.execute("SELECT voice_request FROM voice_request_history ORDER BY id DESC LIMIT 10")
        result = self.cursor.fetchall()
        return result if result else None

    def close(self):
        self.conn.close()

