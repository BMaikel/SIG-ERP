import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("limpieza_total.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def buscar_usuario(self, usuario, password):
        sql = f"""SELECT * FROM empleado WHERE usuario = "{usuario}" AND contraseña = "{password}";"""
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone() #Un registro

        except Exception as e:
            raise
    
    def get_user(self, id):
        sql = f"""SELECT * FROM empleado WHERE id = "{id}";"""
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone() #Un registro

        except Exception as e:
            raise
        
    def close(self):
        self.connection.close() #Es necesario terminar la conección con la base de datos