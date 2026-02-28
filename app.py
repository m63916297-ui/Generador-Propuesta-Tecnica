import gradio as gr
from agent import crear_agente

agente = None


def inicializar_agente(modelo: str, temperatura: float):
    global agente
    try:
        agente = crear_agente(model_name=modelo, temperature=temperatura)
        return "Agente inicializado correctamente"
    except Exception as e:
        return f"Error al inicializar: {str(e)}"


def generar_propuesta(necesidad: str, modelo: str, temperatura: float):
    global agente

    if not necesidad or len(necesidad.strip()) < 10:
        return "Por favor, proporciona una descripción más detallada de la necesidad de negocio (mínimo 10 caracteres)."

    if agente is None:
        try:
            agente = crear_agente(model_name=modelo, temperature=temperatura)
        except Exception as e:
            return f"Error al inicializar el agente: {str(e)}\n\nAsegúrate de tener la variable de entorno OPENAI_API_KEY configurada."

    try:
        propuesta = agente.generar_propuesta(necesidad_negocio=necesidad)
        return propuesta
    except Exception as e:
        return f"Error al generar la propuesta: {str(e)}"


with gr.Blocks(title="Generador de Propuestas Técnicas", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 📝 Generador de Propuestas Técnicas")
    gr.Markdown(
        "Transforma necesidades de negocio ambiguas en propuestas técnicas estructuradas y profesionales."
    )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Configuración")
            modelo = gr.Dropdown(
                choices=["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
                value="gpt-4o-mini",
                label="Modelo",
                info="Modelo de OpenAI a utilizar",
            )
            temperatura = gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=0.7,
                step=0.1,
                label="Temperatura",
                info="Controla la creatividad de las respuestas",
            )
            btn_init = gr.Button("Inicializar Agente", variant="secondary")
            status_init = gr.Textbox(label="Estado", interactive=False)

            btn_init.click(
                fn=inicializar_agente, inputs=[modelo, temperatura], outputs=status_init
            )

        with gr.Column(scale=2):
            gr.Markdown("### Descripción de la Necesidad")
            necesidad_input = gr.Textbox(
                label="Necesidad de Negocio",
                placeholder="Ejemplo: Nuestra empresa necesita optimizar el proceso de atención al cliente que actualmente toma demasiado tiempo...",
                lines=5,
                info="Describe brevemente la necesidad o problema de negocio",
            )

            btn_generar = gr.Button("🚀 Generar Propuesta", variant="primary")

    gr.Markdown("---")

    with gr.Row():
        gr.Markdown("### Propuesta Técnica Generada")

    propuesta_output = gr.Markdown(
        value="*La propuesta técnica aparecerá aquí después de generar...*",
        elem_id="propuesta-output",
    )

    btn_generar.click(
        fn=generar_propuesta,
        inputs=[necesidad_input, modelo, temperatura],
        outputs=propuesta_output,
    )

    gr.Markdown("---")
    gr.Markdown("""
    ### Estructura de la Propuesta
    La propuesta generada incluye:
    1. **Pro - Análisis del gap entre situación actual y deseada
    2blema Identificado**. **Solución Técnica Sugerida** - Componentes, tecnologías y flujo de datos
    3. **Arquitectura General** - Componentes, interacciones y capas
    4. **Principales Riesgos** - Riesgos técnicos e implementaciones con mitigaciones
    """)

app.launch(server_name="0.0.0.0", server_port=7860)
