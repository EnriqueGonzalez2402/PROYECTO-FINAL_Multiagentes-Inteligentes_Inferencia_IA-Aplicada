import streamlit as st

# -----------------------------------
# Configuración de la página
# -----------------------------------

st.set_page_config(
    page_title="AURA",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# Título
# -----------------------------------

st.title("🤖 AURA")
st.subheader("Sistema Experto Multiagente para Diagnóstico de Redes Acústicas ESP32")

st.divider()

# -----------------------------------
# Configuración
# -----------------------------------

st.sidebar.header("⚙ Configuración")

num_nodos = st.sidebar.number_input(
    "Número de nodos esperados",
    min_value=1,
    value=3
)

distancia_ref = st.sidebar.number_input(
    "Distancia de referencia (m)",
    min_value=0.1,
    value=2.0
)

tolerancia = st.sidebar.number_input(
    "Tolerancia permitida (m)",
    min_value=0.01,
    value=0.10
)

# -----------------------------------
# Estado General
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Nodos Esperados",
        num_nodos
    )

with col2:
    st.metric(
        "Nodos Conectados",
        2
    )

with col3:
    st.metric(
        "Distancia Referencia",
        f"{distancia_ref} m"
    )

st.divider()

# -----------------------------------
# Estado de la red
# -----------------------------------

st.header("🌐 Estado de la Red")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🤖 Nodo 1 - Conectado")

with col2:
    st.success("🤖 Nodo 2 - Conectado")

with col3:
    st.error("❌ Nodo 3 - Desconectado")

st.divider()

# -----------------------------------
# Diagnóstico
# -----------------------------------

st.header("🧠 Diagnóstico Actual")

st.info("""
Agente 1 detectó 2 de 3 nodos conectados.

Nodo 3 no responde.

Se recomienda verificar alimentación o comunicación.
""")

st.divider()

# -----------------------------------
# ChatBot
# -----------------------------------

st.header("💬 ChatBot AURA")

pregunta = st.text_input(
    "Consulta al sistema"
)

if pregunta:

    respuesta = f"""
Estado actual:

• Nodos esperados: {num_nodos}
• Nodos conectados: 2
• Nodo desconectado: Nodo 3

Diagnóstico preliminar:
Existe al menos un nodo fuera de servicio.
"""

    st.success(respuesta)