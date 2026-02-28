"""
Generador de Propuestas Técnicas - App Streamlit
Sin API key - Usa templates predefinidos + LangChain Skills
"""

import streamlit as st

from agent import (
    EstadoEjecucion,
    GeneradorPropuestas,
    crear_agente,
    listar_areas_disponibles,
)
from langchain_skills import (
    LangChainSkills,
    TipoArquitectura,
    PatronOrquestacion,
    crear_skills,
)

if "agente" not in st.session_state:
    st.session_state.agente = crear_agente()

if "skills" not in st.session_state:
    st.session_state.skills = crear_skills()

if "historial" not in st.session_state:
    st.session_state.historial = []


EJEMPLOS = {
    "fintech": {
        "input": "Nuestra fintech necesita procesar pagos en tiempo real con cumplimiento PCI-DSS, detección de fraude y soporte para múltiples métodos de pago.",
        "area": "fintech",
    },
    "app_moviles": {
        "input": "Queremos desarrollar una aplicación móvil para que nuestros clientes puedan gestionar sus cuentas y hacer transferencias.",
        "area": "app_moviles",
    },
    "blockchain": {
        "input": "Necesitamos crear un sistema de trazabilidad para productos agrícolas que certifique el origen.",
        "area": "blockchain",
    },
    "arquitectura": {
        "input": "Tenemos un monolito legacy que queremos migrar a microservicios para escalar mejor.",
        "area": "arquitectura",
    },
    "seguros": {
        "input": "Nuestra aseguradora quiere digitalizar el proceso de cotización y emisión de pólizas.",
        "area": "seguros",
    },
    "medica": {
        "input": "Necesitamos un sistema integral para gestionar pacientes, citas y historiales clínicos.",
        "area": "medica",
    },
    "telecomunicaciones": {
        "input": "Como operador necesitamos monitorear la red en tiempo real y automatizar provisioning.",
        "area": "telecomunicaciones",
    },
    "transporte": {
        "input": "Tenemos una flota de 50 camiones y necesitamos optimizar rutas y tracking en tiempo real.",
        "area": "transporte",
    },
    "almacenamiento": {
        "input": "Nuestra bodega tiene problemas con el inventario y queremos optimizar ubicaciones.",
        "area": "almacenamiento",
    },
    "combustibles": {
        "input": "Gestionamos 20 estaciones de servicio y necesitamos monitorear niveles de tanques.",
        "area": "combustibles",
    },
}


def mostrar_trazabilidad(trazabilidad):
    """Muestra la trazabilidad de la ejecución"""
    with st.expander("🔍 Ver trazabilidad de ejecución", expanded=False):
        resumen = trazabilidad.obtener_resumen()

        col1, col2, col3 = st.columns(3)
        col1.metric("Inicio", resumen["inicio"][11:19] if resumen["inicio"] else "-")
        col2.metric("Duración", f"{resumen['duracion_ms']} ms")
        col3.metric("Pasos", resumen["total_pasos"])

        if resumen["total_errores"] > 0:
            st.error(f"Errores: {resumen['total_errores']}")

        st.markdown("### Flujo de ejecución:")
        for i, paso in enumerate(trazabilidad.pasos, 1):
            icon = (
                "✅"
                if paso["estado"] == "completado"
                else "⏳"
                if paso["estado"] != "error"
                else "❌"
            )
            st.markdown(f"{icon} **{i}. {paso['estado'].replace('_', ' ').title()}**")
            st.markdown(f"   - {paso['detalle']}")

        if trazabilidad.errores:
            st.markdown("### Errores:")
            for error in trazabilidad.errores:
                st.markdown(f"- **{error['tipo']}**: {error['mensaje']}")


def mostrar_documentacion():
    """Muestra la documentación del sistema"""
    with st.expander("📚 Documentación del Sistema", expanded=False):
        st.markdown("""
        ## Flujo de Ejecución del Agente
        
        El agente sigue estos pasos:
        
        ### 1. Recepción de Entrada
        - Recibe una descripción corta de la necesidad de negocio
        - Valida que tenga al menos 10 caracteres
        
        ### 2. Detección de Área
        - Analiza palabras clave en la descripción
        - Identifica el área más relevante
        
        ### 3. Identificación del Problema
        - Extrae palabras clave específicas
        - Combina el problema base del template con la necesidad específica
        
        ### 4. Generación de Solución
        - Propone componentes técnicos específicos
        - Recomienda tecnologías apropiadas
        
        ### 5. Diseño de Arquitectura
        - Arquitectura de alto nivel predefinida por área
        
        ### 6. Análisis de Riesgos
        - Identifica riesgos técnicos con mitigaciones
        
        ### 7. Generación de Output
        - Formatea la propuesta en Markdown estructurado
        
        ---
        
        ## Áreas Disponibles
        
        - **Fintech**: Pagos, banca, crédito
        - **App Móviles**: iOS, Android, multiplataforma
        - **Blockchain**: Smart contracts, tokens, Web3
        - **Arquitectura**: Microservicios, cloud, serverless
        - **Seguros**: Pólizas, reclamos, tarificación
        - **Médica**: EHR, telemedicina
        - **Telecomunicaciones**: OSS/BSS, redes
        - **Transporte**: TMS, flotas
        - **Almacenamiento**: WMS, inventario
        - **Combustibles**: Estaciones, tanques
        """)


st.set_page_config(
    page_title="Generador de Propuestas Técnicas", page_icon="📝", layout="wide"
)

st.title("📝 Generador de Propuestas Técnicas")
st.markdown("""
Este sistema genera propuestas técnicas estructuradas sin necesidad de API key.
Incluye **LangChain Skills** para arquitectura y orquestación de agentes.
""")

tab1, tab2, tab3 = st.tabs(["💡 Propuestas", "🏗️ Arquitectura", "🔄 Orquestación"])

with tab1:
    with st.sidebar:
        st.header("⚙️ Configuración")

        area_seleccionada = st.selectbox(
            "Área específica (opcional)",
            ["Auto-detectar"] + listar_areas_disponibles(),
            help="Fuerza un área específica o deja en auto-detectar",
        )

        ver_trazabilidad = st.toggle(
            "Mostrar trazabilidad",
            value=True,
            help="Muestra el flujo de ejecución del agente",
        )

        st.divider()

        st.markdown("### 📋 Cargar Ejemplo")
        ejemplo_seleccionado = st.selectbox(
            "Seleccionar ejemplo",
            list(EJEMPLOS.keys()),
            format_func=lambda x: f"{EJEMPLOS[x]['area'].upper()} - {x.title()}",
        )

        if st.button("Cargar Ejemplo"):
            st.session_state.necesidad_input = EJEMPLOS[ejemplo_seleccionado]["input"]
            st.session_state.area_ejemplo = EJEMPLOS[ejemplo_seleccionado]["area"]

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("📋 Necesidad de Negocio")

        necesidad_input = st.text_area(
            "Describe tu necesidad o problema:",
            value=st.session_state.get("necesidad_input", ""),
            placeholder="Ejemplo: Nuestra empresa necesita optimizar el proceso de atención al cliente...",
            height=200,
            help="Describe brevemente la necesidad de negocio (mínimo 10 caracteres)",
        )

        generar = st.button(
            "🚀 Generar Propuesta",
            type="primary",
            use_container_width=True,
            disabled=not necesidad_input,
        )

    with col2:
        st.header("📄 Propuesta Técnica")

        if generar and necesidad_input:
            if len(necesidad_input.strip()) < 10:
                st.error("La descripción debe tener al menos 10 caracteres")
            else:
                area = (
                    None if area_seleccionada == "Auto-detectar" else area_seleccionada
                )

                with st.spinner("Generando propuesta..."):
                    resultado = st.session_state.agente.generar_propuesta(
                        necesidad=necesidad_input,
                        area_especifica=area,
                        incluir_trazabilidad=ver_trazabilidad,
                    )

                    if resultado.exitoso:
                        st.success(
                            f"✅ Propuesta generada - Área: **{resultado.area_detectada.upper()}**"
                        )
                        st.markdown(resultado.propuesta)

                        if ver_trazabilidad and resultado.trazabilidad:
                            mostrar_trazabilidad(resultado.trazabilidad)

                        st.session_state.historial.append(
                            {
                                "necesidad": necesidad_input,
                                "area": resultado.area_detectada,
                                "propuesta": resultado.propuesta,
                            }
                        )
                    else:
                        st.error(f"❌ Error: {resultado.error}")
                        if ver_trazabilidad and resultado.trazabilidad:
                            mostrar_trazabilidad(resultado.trazabilidad)

        elif not necesidad_input:
            st.info("👆 Ingresa una necesidad de negocio o selecciona un ejemplo")

    if len(st.session_state.historial) > 0:
        st.divider()
        st.markdown("### 📜 Historial de Propuestas")

        for i, item in enumerate(reversed(st.session_state.historial[-5:]), 1):
            with st.expander(
                f"Propuesta {len(st.session_state.historial) - i + 1}: {item['area'].upper()}",
                expanded=False,
            ):
                st.markdown(f"**Input:** {item['necesidad'][:100]}...")
                st.markdown(item["propuesta"])


with tab2:
    st.header("🏗️ Generador de Arquitectura LangChain")
    st.markdown(
        "Genera arquitecturas técnicas detalladas con diagramas usando **LangChain Architecture Skills**."
    )

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Configuración de Arquitectura")

        tipo_arquitectura = st.selectbox(
            "Tipo de Arquitectura",
            [t.value for t in TipoArquitectura],
            format_func=lambda x: x.replace("_", " ").title(),
        )

        contexto = st.text_area(
            "Contexto del proyecto",
            placeholder="Sistema de pagos en tiempo real con alta disponibilidad...",
            height=100,
        )

        servicios_input = st.text_input(
            "Servicios (separados por coma)", placeholder="usuarios, pagos, reportes"
        )

        generar_arquitectura = st.button(
            "🏗️ Generar Arquitectura", type="primary", use_container_width=True
        )

    with col2:
        if generar_arquitectura and contexto:
            tipo_enum = TipoArquitectura(tipo_arquitectura)
            servicios = [s.strip() for s in servicios_input.split(",") if s.strip()]

            with st.spinner("Generando arquitectura..."):
                resultado = st.session_state.skills.generar_arquitectura_completa(
                    tipo=tipo_enum, contexto=contexto, servicios=servicios
                )

                st.success("✅ Arquitectura generada")

                st.markdown("### 📐 Diagrama de Arquitectura")
                st.markdown(resultado["diagrama"])

                st.markdown(resultado["resumen"])

        else:
            st.info("👆 Configura la arquitectura y genera el diagrama")

            with st.expander("📋 Tipos de Arquitectura"):
                st.markdown("""
                - **Microservicios**: Servicios independientes que se comunican via API
                - **Serverless**: Funciones como servicio (Lambda, Cloud Functions)
                - **Event Driven**: Arquitectura basada en eventos y mensajería
                - **Monolito**: Aplicación única todo en uno
                - **Híbrida**: Combinación de varios enfoques
                """)


with tab3:
    st.header("🔄 Orquestación de Agentes LangChain")
    st.markdown(
        "Diseña patrones de orquestación para agentes especializados con **LangChain Orchestration Skills**."
    )

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### Configuración de Orquestación")

        patron = st.selectbox(
            "Patrón de Orquestación",
            [p.value for p in PatronOrquestacion],
            format_func=lambda x: x.replace("_", " ").title(),
        )

        necesidad_orquestacion = st.text_area(
            "Necesidad o requerimiento",
            placeholder="Sistema que requiera múltiples agentes especializados...",
            height=80,
        )

        incluir_arquitectura = st.checkbox(
            "Incluir generación de arquitectura", value=True
        )

        generar_orquestacion = st.button(
            "🔄 Generar Plan", type="primary", use_container_width=True
        )

    with col2:
        if generar_orquestacion and necesidad_orquestacion:
            patron_enum = PatronOrquestacion(patron)

            with st.spinner("Generando plan de orquestación..."):
                resultado_orq = (
                    st.session_state.skills.orquestacion.generar_plan_ejecucion(
                        necesidad=necesidad_orquestacion, patron=patron_enum
                    )
                )

                st.success("✅ Plan de orquestación generado")

                st.markdown("### 📋 Plan de Ejecución")
                st.markdown(f"**Patrón:** {patron.replace('_', ' ').title()}")
                st.markdown(f"**Descripción:** {resultado_orq.get('descripcion', '')}")

                st.markdown("#### Pasos:")
                for paso in resultado_orq.get("pasos", []):
                    if "agentes" in paso:
                        st.markdown(
                            f"- **{paso.get('orden', '')}**. {paso['descripcion']}"
                        )
                        st.markdown(f"  - Agentes: {', '.join(paso['agentes'])}")
                    else:
                        st.markdown(
                            f"- **{paso.get('orden', '')}**. {paso['descripcion']}"
                        )
                        st.markdown(f"  - Agente: {paso.get('agente', 'N/A')}")

                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("#### ✅ Ventajas")
                    for v in resultado_orq.get("ventajas", []):
                        st.markdown(f"- {v}")

                with col_b:
                    st.markdown("#### ⚠️ Desventajas")
                    for d in resultado_orq.get("desventajas", []):
                        st.markdown(f"- {d}")

                if incluir_arquitectura:
                    st.markdown("---")
                    st.markdown("### 🏗️ Arquitectura Sugerida")

                    tipo_arq = (
                        TipoArquitectura.MICROSERVICIOS
                        if "microservicio" in necesidad_orquestacion.lower()
                        else TipoArquitectura.SERVERLESS
                    )

                    resultado_arq = (
                        st.session_state.skills.generar_arquitectura_completa(
                            tipo=tipo_arq, contexto=necesidad_orquestacion, servicios=[]
                        )
                    )

                    st.markdown(resultado_arq["diagrama"])

        else:
            st.info("👆 Configura el patrón de orquestación")

            with st.expander("📋 Patrones de Orquestación"):
                st.markdown("""
                - **Secuencial**: Agentes ejecutan uno después de otro
                - **Paralelo**: Todos los agentes ejecutan concurrentemente
                - **Jerárquico**: Un manager coordina trabajadores
                - **Consumer/Producer**: Productores de eventos y consumidores
                """)

            with st.expander("👥 Agentes Disponibles"):
                st.markdown("""
                - **Analista**: Analiza y documenta necesidades
                - **Arquitecto**: Diseña arquitectura técnica
                - **Desarrollador**: Implementa código
                - **QA**: Diseña pruebas y validación
                - **DevOps**: Infraestructura y despliegue
                """)


with st.sidebar:
    st.divider()
    if st.button("📚 Ver Documentación"):
        mostrar_documentacion()
