# Generador de Propuestas Técnicas

Transforma necesidades de negocio ambiguas en propuestas técnicas estructuradas y profesionales usando LangChain y OpenAI.

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT / GRADIO                       │
│                        (UI Layer)                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  app.py / app_streamlit.py                          │   │
│  │  - Interfaz de usuario                              │   │
│  │  - Validación de entrada                            │   │
│  │  - Manejo de errores                                │   │
│  └────────────────────────┬──────────────────────────────┘   │
│                           │                                  │
│                           ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   agent.py                           │   │
│  │              (Business Logic Layer)                 │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │   │
│  │  │ ChatOpenAI │  │ LLMChain    │  │   Prompt    │  │   │
│  │  │            │◄─┤             │◄─┤  Template   │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │   │
│  └────────────────────────┬──────────────────────────────┘   │
└─────────────────────────────┼───────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   OPENAI API    │
                    │  (GPT Models)   │
                    └─────────────────┘
```

### Capas

| Capa | Archivo | Responsabilidad |
|------|---------|------------------|
| **UI** | `app.py` / `app_streamlit.py` | Interfaz, validación input, rendering |
| **Business Logic** | `agent.py` | LLMChain, generación de propuestas |
| **Prompts** | `prompts.py` | Templates de prompts |

---

## 🚀 Quick Start

### Local

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar API Key
export OPENAI_API_KEY="sk-..."

# 3. Ejecutar
streamlit run app_streamlit.py
# o
python app.py
```

### Streamlit Cloud

1. Subir código a GitHub
2. Configurar secrets en Streamlit Cloud:
   ```
   OPENAI_API_KEY = "sk-..."
   ```
3. Apuntar a `app_streamlit.py` como main file

---

## 📁 Estructura de Archivos

```
generador/
├── app.py                 # Interfaz Gradio (original)
├── app_streamlit.py       # Interfaz Streamlit
├── agent.py               # Lógica del agente LangChain
├── prompts.py             # Templates de prompts
├── rules.md               # Reglas del proyecto
├── workflow.md            # Diagramas de flujo
├── README.md              # Este archivo
└── requirements.txt       # Dependencias Python
```

---

## ⚙️ Configuración

### Modelos Disponibles

| Modelo | Uso recomendado |
|--------|-----------------|
| `gpt-4o-mini` | Rápido, económico |
| `gpt-4o` | Mejor calidad |
| `gpt-3.5-turbo` | Compatibilidad |

### Parámetros

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| `temperature` | 0.0 - 1.0 | 0.7 | Creatividad de respuestas |

---

## 📋 Estructura de la Propuesta

La propuesta generada incluye:

1. **Problema Identificado** - Análisis del gap entre situación actual y deseada
2. **Solución Técnica Sugerida** - Componentes, tecnologías y flujo de datos
3. **Arquitectura General** - Componentes, interacciones y capas
4. **Principales Riesgos** - Riesgos técnicos e implementaciones con mitigaciones

---

## 🔧 Desarrollo

### Reglas del Proyecto

Ver `rules.md` para reglas de:
- Configuración de modelos
- Validación de entrada
- Estructura de propuesta
- Manejo de errores
- Configuración Streamlit Cloud

### Workflow

Ver `workflow.md` para:
- Diagramas de flujo de usuario
- Diagrama técnico LangChain
- Pasos de despliegue

---

## 📝 Licencia

MIT
