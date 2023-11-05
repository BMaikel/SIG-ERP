import sqlite3

conn = sqlite3.connect("limpieza_total.db")
cursor = conn.cursor()

#Creamdo tabla PRODUCTOS -----------------------------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS producto (
               id VARCHAR(5) PRIMARY KEY,
               nombre VARCHAR(128) NOT NULL,
               marca VARCHAR(128) NOT NULL,
               precio REAL NOT NULL,
               categoria VARCHAR(128) NOT NULL,
               img TEXT NOT NULL);""")

#Creando tabla INVENTARIO ----------------------------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS inventario (
               id_producto VARCHAR(5) PRIMARY KEY,
               cantidad INTEGER NOT NULL);""")

#Creando tabla PROVEEDOR -----------------------------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS proveedor (
               id VARCHAR(5) PRIMARY KEY,
               nombre VARCHAR(128) NOT NULL,
               direccion VARCHAR(256) NOT NULL,
               cel VARCHAR(128) NOT NULL);""")

#Creando tabla EMPLEADOS -----------------------------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS empleado (
               id VARCHAR(5) PRIMARY KEY,
               nombres VARCHAR(128) NOT NULL,
               apellidos VARCHAR(128) NOT NULL,
               cel VARCHAR(128) NOT NULL,
               usuario VARCHAR(128) NOT NULL,
               contraseña VARCHAR(128) NOT NULL);""")

#Creando tabla CLIENTES -----------------------------------------------------------------------
cursor.execute("""CREATE TABLE IF NOT EXISTS cliente (
               id VARCHAR(5) PRIMARY KEY,
               nombre VARCHAR(128) NOT NULL,
               direccion VARCHAR(256) NOT NULL,
               cel VARCHAR(128) NOT NULL,
               tipo VARCHAR(128) NOT NULL);""")

productos = [
    (1,"Desinfectante x Galón", "DARYZA", 18.5, "DESINFECTANTES","https://i0.wp.com/grupocasalima.com/wp-content/uploads/2022/10/desinfectante-por-galon.webp?fit=900%2C900&ssl=1"),
    (2,"Alcohol en Gel 3.5 Lt", "NACIONAL", 45.0, "ALCOHOL", "https://i0.wp.com/grupocasalima.com/wp-content/uploads/2022/08/alcohol-en-gel-3-5-lt.webp?fit=900%2C900&ssl=1"),
    (3,"Bolsa Marrón de 140 Litros (100 Unidades)", "NACIONAL", 42.0, "BOLSAS", "https://i0.wp.com/grupocasalima.com/wp-content/uploads/2022/11/bolsa-de-basura-marron.webp?fit=900%2C900&ssl=1"),
    (4,"Detergente de 14 Kg", "SAPOLIO", 82.0, "DETERGENTES", "https://i0.wp.com/grupocasalima.com/wp-content/uploads/2022/09/detergente-sapolio.webp?fit=900%2C900&ssl=1"),
    (5, "Paño Absorbente X 6 Uni  Brite", "SCOTCH BRITE", 14.0, "PAÑOS", "https://i0.wp.com/grupocasalima.com/wp-content/uploads/2022/08/pano-absorbente-scotch-brite.webp?fit=900%2C900&ssl=1"),
    (6, "Guante antideslizante 2 capas", "ETERNA", 8.0, "GUANTES DE JEBE", "https://i0.wp.com/grupocasalima.com/wp-content/uploads/2022/07/guante-antideslizante-2.webp?fit=900%2C900&ssl=1")
]

empleados = [
    (1, "Maicol Alexis", "Bañares Gutierrez", "982301518", "admin", "admin"),
    (2,"Jhordy Alexander", "Castro Fernandez", "960794457", "user1", "user1"),
]

inventario = [
    (1,2),
    (2,5),
    (3,3),
    (4,2),
    (5,3),
    (6,4)
]

proveedores = [
    (1, "DISTRIBUIDORA NIASGI E.I.R.L", "Urb Cinco Estrellas Mz B Lt 24, Ate 15770", "983526105"),
    (2, "QUIMICOS G Y P DISTRIBUIDORA S.A.C", "51, C. Las Palomas 120, Surquillo 15048", "980 316 131"),
    (3, "AKU PRODUCTOS DE LIMPIEZA", "Carr. Central 460, Chaclacayo 15472", "922862669")
]

clientes = [
    (1, "CORTINAS TAPICERIAS XANDER", "JR. PASCO 3699 URB. PERU", "946360697", "EMPRESA")
]

cursor.executemany("INSERT INTO producto VALUES (?,?,?,?,?,?)", productos)
cursor.executemany("INSERT INTO inventario VALUES (?,?)", inventario)
cursor.executemany("INSERT INTO empleado VALUES (?,?,?,?,?,?)", empleados)
cursor.executemany("INSERT INTO proveedor VALUES (?,?,?,?)", proveedores)
cursor.executemany("INSERT INTO cliente VALUES (?,?,?,?,?)", clientes)


conn.commit()
conn.close()