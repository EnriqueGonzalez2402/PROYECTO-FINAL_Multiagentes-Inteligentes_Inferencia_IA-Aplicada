import sqlite3

DB_NAME = "aura.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

# -----------------------------
# Guardar configuración
# -----------------------------
def save_configuration(
    num_nodos,
    distancia_referencia,
    tolerancia
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM configuracion")

    cursor.execute("""
        INSERT INTO configuracion
        (
            num_nodos,
            distancia_referencia,
            tolerancia
        )
        VALUES (?, ?, ?)
    """,
    (
        num_nodos,
        distancia_referencia,
        tolerancia
    ))

    conn.commit()
    conn.close()

# -----------------------------
# Obtener configuración
# -----------------------------
def get_configuration():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            num_nodos,
            distancia_referencia,
            tolerancia
        FROM configuracion
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return row