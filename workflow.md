# Workflow - Generador de Propuestas Técnicas

## Flujo de Usuario

```
┌─────────────────────────────────────────────────────────────┐
│                     INICIO DEL FLUJO                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  1. CONFIGURACIÓN (Sidebar)                                │
│     ├── Seleccionar modelo (gpt-4o-mini, gpt-4o, etc.)     │
│     ├── Ajustar temperatura (0.0 - 1.0)                     │
│     └── (Opcional) Inicializar agente explícitamente        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  2. INPUT - Necesidad de Negocio                            │
│     └── Usuario ingresa descripción del problema/necesidad  │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  3. VALIDACIÓN                                             │
│     ├── ¿Entrada vacía? → Mostrar error                     │
│     └── ¿Menos de 10 caracteres? → Mostrar error            │
└─────────────────────────┬───────────────────────────────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
         [ERROR]              [VALIDADO]
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  4. INICIALIZACIÓN DEL AGENTE (si no existe)                │
│     ├── Verificar OPENAI_API_KEY                            │
│     ├── Crear ChatOpenAI con modelo y temperatura           │
│     └── Crear LLMChain con prompt predefinido               │
└─────────────────────────┬───────────────────────────────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
         [ERROR]              [ÉXITO]
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  5. GENERACIÓN DE PROPUESTA                                 │
│     ├── Enviar necesidad al LLMChain                        │
│     ├── LLM procesa con PromptTemplate                      │
│     └── Retornar propuesta estructurada                      │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  6. OUTPUT - Mostrar Propuesta                              │
│     └── Renderizar Markdown en Streamlit                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Flujo Técnico (LangChain)

```
┌──────────────────────────────────────────────┐
│           PromptTemplate                      │
│  (prompts.py - PROMPT_TEMPLATE)             │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│            ChatOpenAI                        │
│  (gpt-4o-mini/gpt-4o + temperature)          │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│              LLMChain                        │
│  (Combina prompt + llm + output parser)      │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│         Output (Propuesta Markdown)          │
└──────────────────────────────────────────────┘
```

---

## Despliegue en Streamlit Cloud

### Pasos de Configuración

1. **Preparar archivos**:
   - `app.py` → versión Streamlit
   - `agent.py` → sin cambios
   - `prompts.py` → sin cambios
   - `requirements.txt` → actualizado

2. **Configurar Secrets** (Streamlit Cloud):
   ```
   OPENAI_API_KEY = "sk-..."
   ```

3. **Configuración en Streamlit Cloud**:
   - Repository: GitHub repo
   - Branch: main
   - Python version: 3.11
   - Requirements file: requirements.txt

---

## Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT CLOUD                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   app.py (Streamlit)                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │   │
│  │  │  Sidebar   │  │   Input     │  │   Output    │  │   │
│  │  │(Config)    │  │(Text Area)  │  │ (Markdown)  │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │   │
│  └────────────────────────┬────────────────────────────┘   │
│                           │                                │
│                           ▼                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              agent.py (LangChain)                   │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │   │
│  │  │ ChatOpenAI │  │ LLMChain    │  │   Prompt    │  │   │
│  │  │            │◄─┤             │◄─┤  Template   │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │   │
│  └────────────────────────┬────────────────────────────┘   │
└─────────────────────────────┼───────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   OPENAI API    │
                    │  (GPT Models)   │
                    └─────────────────┘
```
