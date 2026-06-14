import sqlite3

conn = sqlite3.connect("aura.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS configuracion(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num_nodos INTEGER,
    distancia_referencia REAL,
    tolerancia REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS nodos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    estado TEXT,
    ultima_conexion TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS mediciones(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nodo_a TEXT,
    nodo_b TEXT,
    rtt REAL,
    tof REAL,
    distancia REAL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inferencias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    regla TEXT,
    resultado TEXT,
    explicacion TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS historial(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agente TEXT,
    evento TEXT,
    resultado TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Base de datos creada correctamente")