"""Manage database connection"""
import sqlite3


class DB:
    connection = None

    def __init__(self, db: str):
        if self.connection is None:
            self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def query(self, sql: str, params: list, commit=False):
        self.cursor.execute(sql, params)
        if commit:
            self.connection.commit()
        return self.cursor

    def close(self):
        self.connection.close()
