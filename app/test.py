from bd_cnn import Database

db = Database()

a = db.buscar_usuario("admin","admin")
db.close