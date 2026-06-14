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

# -----------------------------
# Guardar evento en historial
# -----------------------------
def save_history(
    agente,
    evento,
    resultado
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO historial
        (
            agente,
            evento,
            resultado
        )
        VALUES (?, ?, ?)
    """,
    (
        agente,
        evento,
        resultado
    ))

    conn.commit()
    conn.close()

# -----------------------------
# Obtener historial
# -----------------------------
def get_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            fecha,
            agente,
            evento,
            resultado
        FROM historial
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

