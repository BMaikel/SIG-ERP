import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("limpieza_total.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def ver_productos(self):
        sql = f"""SELECT * FROM producto"""
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall() #Todos los registros

        except Exception as e:
            raise