# Rules - Generador de Propuestas Técnicas

## Propósito
Transformar necesidades de negocio ambiguas en propuestas técnicas estructuradas y profesionales usando LangChain y OpenAI.

---

## Reglas de Configuración

### 1. Modelos y Parámetros
- **Modelos disponibles**: `gpt-4o-mini`, `gpt-4o`, `gpt-3.5-turbo`
- **Temperatura**: Rango 0.0 - 1.0 (default: 0.7)
- **API Key**: Requiere variable de entorno `OPENAI_API_KEY`

### 2. Dependencias
```
langchain
langchain-openai
streamlit
python-dotenv
```

---

## Reglas de Negocio

### 3. Validación de Entrada
- La necesidad de negocio debe tener **mínimo 10 caracteres**
- Si está vacía o es muy corta, mostrar mensaje de error claro

### 4. Estructura de la Propuesta
La propuesta DEBE incluir:
1. **Problema Identificado** - Análisis del gap actual vs deseado
2. **Solución Técnica** - Componentes, tecnologías, flujo de datos
3. **Arquitectura General** - Capas, interacciones, responsabilidades
4. **Riesgos y Mitigaciones** - Técnicos, implementación, integración

---

## Reglas Técnicas

### 5. Patrón de LangChain
- Usar `ChatOpenAI` de `langchain-openai`
- Usar `LLMChain` para el chain básico
- Prompt con `PromptTemplate` de `langchain`

### 6. Manejo de Errores
- Capturar excepciones y retornar mensajes descriptivos
- No exponer stack traces al usuario
- Validar API key al inicializar

### 7. Configuración Streamlit Cloud
- Puerto: `8501` (default de Streamlit)
- Secrets: Configurar `OPENAI_API_KEY` en Streamlit Cloud
- `requirements.txt` con todas las dependencias

---

## Reglas de UX/UI

### 8. Interfaz Streamlit
- Título claro con descripción del app
- Sidebar para configuración (modelo, temperatura)
- Área de texto para necesidad de negocio
- Botón para generar propuesta
- Mostrar propuesta en formato Markdown

### 9. Feedback al Usuario
- Mostrar estado de carga durante generación
- Mensajes de error claros y accionables
- Indicador de éxito al inicializar
