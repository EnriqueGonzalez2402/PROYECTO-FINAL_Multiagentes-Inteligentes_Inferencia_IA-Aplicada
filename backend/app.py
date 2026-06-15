import streamlit as st
import pandas as pd

from agents.connectivity_agent import ConnectivityAgent
from agents.localization_agent import LocalizationAgent
from agents.diagnosis_agent import DiagnosisAgent

from database.db import (
    save_configuration,
    get_configuration,
    save_history,
    get_history
)
# -----------------------------------
# Configuración de la página
# -----------------------------------

st.set_page_config(
    page_title="AURA",
    page_icon="🤖",
    layout="wide"
)
config = get_configuration()

if config:

    default_nodes = config[0]
    default_reference = config[1]
    default_tolerance = config[2]

else:

    default_nodes = 3
    default_reference = 2.0
    default_tolerance = 0.10

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
    value=default_nodes
)

distancia_ref = st.sidebar.number_input(
    "Distancia de referencia (m)",
    min_value=0.1,
    value=default_reference
)

tolerancia = st.sidebar.number_input(
    "Tolerancia permitida (m)",
    min_value=0.01,
    value=default_tolerance
)

if st.sidebar.button("💾 Guardar Configuración"):

    save_configuration(
        num_nodos,
        distancia_ref,
        tolerancia
    )

    save_history(
        "Sistema",
        "Configuración actualizada",
        f"Nodos={num_nodos}, Ref={distancia_ref}, Tol={tolerancia}"
    )

    st.sidebar.success(
        "Configuración guardada"
    )

# -----------------------------------
# Agente 1 - Conectividad
# -----------------------------------

agent1 = ConnectivityAgent()

connectivity = agent1.verify_nodes(num_nodos)

connected_nodes = connectivity["connected"]
missing_nodes = connectivity["missing"]
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
        connected_nodes
    )

with col3:
    st.metric(
        "Distancia Referencia",
        f"{distancia_ref} m"
    )

st.divider()

st.header("🤖 Estado de Agentes")

col1, col2, col3 = st.columns(3)

with col1:

    if missing_nodes == 0:

        st.success("✅ Agente 1 - Conectividad")

    else:

        st.warning("⚠️ Agente 1 - Conectividad")

with col2:

    st.info("⏳ Agente 2 - Localización")

with col3:

    st.info("⏳ Agente 3 - Diagnóstico")
# -----------------------------------
# Estado de la red
# -----------------------------------

st.header("🌐 Estado de la Red")

for i in range(1, num_nodos + 1):

    if i <= connected_nodes:

        st.success(f"🤖 Nodo {i} - Conectado")

    else:

        st.error(f"❌ Nodo {i} - Desconectado")

st.divider()

# -----------------------------------
# Diagnóstico
# -----------------------------------

st.header("🧠 Diagnóstico Actual")

if missing_nodes == 0:

    st.success(
        f"Todos los nodos esperados ({num_nodos}) están conectados."
    )

else:

    st.warning(
        f"Se detectaron {connected_nodes} de {num_nodos} nodos. "
        f"Faltan {missing_nodes} nodo(s)."
    )

st.divider()


if st.button("🔍 Verificar Nodos"):

    save_history(
        "Agente 1",
        "Verificación de conectividad",
        f"{connected_nodes}/{num_nodos} nodos detectados"
    )

    st.success("Verificación registrada")


st.divider()

st.header("📡 Agente 2 - Localización Acústica")
rtt = st.number_input(
    "RTT (segundos)",
    min_value=0.001,
    value=0.012,
    step=0.001
)
agent2 = LocalizationAgent()
measurement = agent2.calculate_distance(rtt)

st.metric(
    "ToF",
    f"{measurement['tof']:.6f} s"
)

st.metric(
    "Distancia",
    f"{measurement['distance']} m"
)

st.header("🧠 Agente 3 - Diagnóstico")

agent3 = DiagnosisAgent()
diagnosis = agent3.validate_distance(
    measurement["distance"],
    distancia_ref,
    tolerancia
)

st.write(
    f"Estado: {diagnosis['status']}"
)

st.write(
    f"Error: {diagnosis['error']} m"
)

st.info(
    diagnosis["explanation"]
)

# -----------------------------------
# ChatBot
# -----------------------------------

st.header("💬 ChatBot AURA")

pregunta = st.text_input(
    "Consulta al sistema"
)

if pregunta:

    pregunta = pregunta.lower()

    if "estado" in pregunta:

        respuesta = f"""
Nodos esperados: {num_nodos}

Nodos conectados: {connected_nodes}

Nodos faltantes: {missing_nodes}
"""

    elif "distancia" in pregunta:

        respuesta = f"""
La distancia de referencia actual es:

{distancia_ref} metros
"""

    elif "agente 1" in pregunta:

        respuesta = f"""
Agente 1 detectó:

{connected_nodes} de {num_nodos} nodos.
"""

    else:

        respuesta = """
No entendí la consulta.

Prueba:

- estado
- distancia
- agente 1
"""

    st.success(respuesta)
    

st.divider()

st.header("📜 Historial del Sistema")

history = get_history()

if history:

    import pandas as pd

    df = pd.DataFrame(
        history,
        columns=[
            "Fecha",
            "Agente",
            "Evento",
            "Resultado"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info(
        "No existen registros todavía."
    )