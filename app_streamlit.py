import streamlit as st
from agent import crear_agente

if "agente" not in st.session_state:
    st.session_state.agente = None


def inicializar_agente(modelo: str, temperatura: float):
    try:
        st.session_state.agente = crear_agente(
            model_name=modelo, temperature=temperatura
        )
        return True, "Agente inicializado correctamente"
    except Exception as e:
        return False, f"Error al inicializar: {str(e)}"


def generar_propuesta(necesidad: str, modelo: str, temperatura: float):
    if not necesidad or len(necesidad.strip()) < 10:
        return (
            False,
            "Por favor, proporciona una descripción más detallada de la necesidad de negocio (mínimo 10 caracteres).",
        )

    if st.session_state.agente is None:
        success, message = inicializar_agente(modelo, temperatura)
        if not success:
            return False, message

    try:
        propuesta = st.session_state.agente.generar_propuesta(
            necesidad_negocio=necesidad
        )
        return True, propuesta
    except Exception as e:
        return False, f"Error al generar la propuesta: {str(e)}"


st.set_page_config(
    page_title="Generador de Propuestas Técnicas", page_icon="📝", layout="wide"
)

st.title("📝 Generador de Propuestas Técnicas")
st.markdown(
    "Transforma necesidades de negocio ambiguas en propuestas técnicas estructuradas y profesionales."
)

with st.sidebar:
    st.header("⚙️ Configuración")

    modelo = st.selectbox(
        "Modelo",
        ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
        index=0,
        help="Modelo de OpenAI a utilizar",
    )

    temperatura = st.slider(
        "Temperatura",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Controla la creatividad de las respuestas",
    )

    if st.button("Inicializar Agente", type="secondary"):
        with st.spinner("Inicializando agente..."):
            success, message = inicializar_agente(modelo, temperatura)
            if success:
                st.success(message)
            else:
                st.error(message)

    st.divider()
    st.markdown("""
    ### ℹ️ Notas
    - Asegúrate de configurar `OPENAI_API_KEY` en Streamlit Cloud Secrets
    - La propuesta incluye: Problema, Solución, Arquitectura y Riesgos
    """)

col1, col2 = st.columns([1, 2])

with col1:
    st.header("📋 Necesidad de Negocio")
    necesidad_input = st.text_area(
        "Describe tu necesidad o problema:",
        placeholder="Ejemplo: Nuestra empresa necesita optimizar el proceso de atención al cliente que actualmente toma demasiado tiempo...",
        height=200,
        help="Describe brevemente la necesidad o problema de negocio",
    )

with col2:
    st.header("📄 Propuesta Técnica")

    if st.button("🚀 Generar Propuesta", type="primary", use_container_width=True):
        if not necesidad_input:
            st.warning("Por favor, ingresa una necesidad de negocio")
        else:
            with st.spinner("Generando propuesta..."):
                success, resultado = generar_propuesta(
                    necesidad_input, modelo, temperatura
                )

                if success:
                    st.markdown(resultado)
                else:
                    st.error(resultado)

    if "propuesta" not in locals() and not necesidad_input:
        st.info("La propuesta técnica aparecerá aquí después de generar...")

st.divider()
st.markdown("""
### 📋 Estructura de la Propuesta
La propuesta generada incluye:
1. **Problema Identificado** - Análisis del gap entre situación actual y deseada
2. **Solución Técnica Sugerida** - Componentes, tecnologías y flujo de datos
3. **Arquitectura General** - Componentes, interacciones y capas
4. **Principales Riesgos** - Riesgos técnicos e implementaciones con mitigaciones
""")
