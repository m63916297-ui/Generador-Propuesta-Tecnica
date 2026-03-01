# Generador de Propuestas Técnicas

Transforma necesidades de negocio ambiguas en propuestas técnicas estructuradas y profesionales usando **LangChain** y **Streamlit**.

---

## 🏗️ Arquitectura

La aplicación sigue una arquitectura de **3 capas** claramente definida:

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT (UI Layer)                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  app_streamlit.py                                    │   │
│  │  - Interfaz de usuario                                │   │
│  │  - Validación de entrada                              │   │
│  │  - Manejo de errores UI                               │   │
│  │  - Trazabilidad visual                                │   │
│  └────────────────────────┬──────────────────────────────┘   │
│                           │                                  │
│                           ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │     LangChain Skills (Orquestación y Templates)     │   │
│  │  ┌─────────────────┐  ┌─────────────────────────┐  │   │
│  │  │ langchain_skills│  │     templates.py        │  │   │
│  │  │ (Orquestación) │  │ (Lógica de Negocio)     │  │   │
│  │  └────────┬────────┘  └───────────┬─────────────┘  │   │
│  └───────────┼───────────────────────┼─────────────────┘   │
│              │                       │                      │
│              ▼                       ▼                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   agent.py                            │   │
│  │              (Business Logic Layer)                 │   │
│  │  - GeneradorPropuestas                               │   │
│  │  - Trazabilidad                                      │   │
│  │  - Manejo de errores                                 │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Capas de la Arquitectura

| Capa | Archivo | Responsabilidad |
|------|---------|-----------------|
| **UI (Presentación)** | `app_streamlit.py` | Interfaz de usuario, validación input, rendering, visualización de trazabilidad |
| **Orquestación** | `langchain_skills.py` | Patrones de arquitectura (Microservicios, Serverless, Event-Driven), orquestación de agentes (Secuencial, Paralelo, Jerárquico) |
| **Lógica de Negocio** | `agent.py`, `templates.py` | Generación de propuestas, detección de áreas, templates por sector |

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión/Tipo |
|------------|------------|--------------|
| **Frontend UI** | Streamlit | Interfaz web interactiva |
| **Framework AI** | LangChain | Orquestación de agentes y skills |
| **Lenguaje** | Python 3.x | Core del sistema |
| **Patrones de Diseño** | Dataclasses, Enums | Estructura de datos |

---

## 📐 Separación entre Orquestación y Lógica de Negocio

### Orquestación (`langchain_skills.py`)

La capa de **orquestación** define **cómo** se ejecutan las tareas:

#### Tipos de Arquitectura Soportados
```python
class TipoArquitectura(Enum):
    MICROSERVICIOS   # Servicios independientes
    SERVERLESS       # Funciones como servicio
    EVENT_DRIVEN    # Basada en eventos
    MONOLITO         # Aplicación única
    HIBRIDA          # Combinación de enfoques
```

#### Patrones de Orquestación de Agentes
```python
class PatronOrquestacion(Enum):
    SECUENCIAL       # Agentes uno después de otro
    PARALELO         # Ejecución concurrente
    JERARQUICO       # Manager coordina workers
    CONSUMER_PRODUCER # Productores y consumidores
```

### Lógica de Negocio (`agent.py`, `templates.py`)

La capa de **lógica de negocio** define **qué** se hace:

#### Generación de Propuestas
- Detección automática de área de negocio (10 sectores)
- Extracción de palabras clave
- Identificación de problemas específicos
- Generación de soluciones técnicas personalizadas
- Diseño de arquitectura por sector
- Análisis de riesgos con mitigaciones

#### Templates por Área
La aplicación incluye **10 templates predefinidos**:
- Fintech, App Móviles, Blockchain, Arquitectura
- Seguros, Médica, Telecomunicaciones, Transporte
- Almacenamiento, Combustibles

---

## ⚠️ Manejo de Errores

El sistema implementa un manejo de errores robusto en dos niveles:

### Nivel de Agente (`agent.py`)

```python
try:
    # Ejecución principal
    trazabilidad.iniciar()
    # ... procesamiento ...
    return ResultadoPropuesta(exitoso=True, ...)
except ValueError as e:
    # Error de validación
    trazabilidad.agregar_error("ValueError", str(e), "Validación de entrada")
    return ResultadoPropuesta(exitoso=False, error=str(e))
except Exception as e:
    # Error inesperado
    trazabilidad.agregar_error("Exception", str(e), "Ejecución del agente")
    return ResultadoPropuesta(exitoso=False, error=f"Error inesperado: {str(e)}")
```

### Validaciones Implementadas

| Validación | Condición | Error |
|------------|-----------|-------|
| Longitud mínima | `len(nec.strip()) < 10` | "La descripción debe tener al menos 10 caracteres" |
| Área específica | No existe en templates | Usa detección automática |
| Input vacío | `not necesidad` | Validación en UI |

### Trazabilidad de Errores

Cada error registrado incluye:
- **Tipo**: Classification del error
- **Mensaje**: Descripción legible
- **Contexto**: Dónde ocurrió
- **Timestamp**: Cuándo ocurrió

---

## 📥 Ejemplos de Input y Output

### Ejemplo 1: Fintech

**Input:**
```
Nuestra fintech necesita procesar pagos en tiempo real con 
cumplimiento PCI-DSS, detección de fraude y soporte para 
múltiples métodos de pago.
```

**Output:**
```markdown
# PROPUESTA TÉCNICA

## Área: Fintech

---

## 1. PROBLEMA IDENTIFICADO

Los procesos financieros tradicionales son lentos, manuales y 
propensos a errores, lackedo de automatización y seguridad.

**Necesidad específica identificada:** Nuestra fintech necesita 
procesar pagos en tiempo real...

**Palabras clave detectadas:** pagos, tiempo real, pci-dss, 
fraude, métodos de pago

---

## 2. SOLUCIÓN TÉCNICA SUGERIDA

Plataforma financiera digital con procesamiento en tiempo real...

**Componentes específicos sugeridos:**
- Procesador de pagos en tiempo real
- Módulo de KYC/AML
- Dashboard de análisis financiero

---

## 3. ARQUITECTURA GENERAL

Arquitectura de microservicios con API Gateway, servicios de 
procesamiento de pagos, módulo de cumplimiento...

### Tecnologías Recomendadas
Python/Django, PostgreSQL, Redis, Kafka, Kubernetes, AWS/GCP, Stripe API

---

## 4. PRINCIPALES RIESGOS

- **Cumplimiento regulatorio**: Integración con servicios de compliance...
- **Fraude financiero**: Sistemas de detección de anomalías...
- **Disponibilidad 24/7**: Arquitectura redundante...
- **Seguridad de datos financieros**: Encriptación en tránsito...
```

---

### Ejemplo 2: Arquitectura de Microservicios

**Input:**
```
Tenemos un monolito legacy que queremos migrar a microservicios 
para escalar mejor.
```

**Output (Diagrama de Arquitectura):**
```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENTES                               │
│   (Web, Mobile, API Consumers)                              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      API GATEWAY                             │
│            (Kong / AWS API Gateway)                         │
└────────────────────────┬────────────────────────────────────┘
                         │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Servicio A  │  │ Servicio B  │  │ Servicio C  │
│  (Core)      │  │  (Business) │  │  (Support)  │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    SERVICE MESH                              │
│              (Istio / Linkerd)                              │
└────────────────────────┬────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   ┌─────────┐    ┌──────────┐   ┌──────────┐
   │PostgreSQL│    │  Redis   │   │  Kafka   │
   │  (Data)  │    │  (Cache)  │   │ (Events) │
   └─────────┘    └──────────┘   └──────────┘
```

---

### Ejemplo 3: Orquestación Jerárquica

**Input:**
```
Sistema que requiera múltiples agentes especializados
```

**Output (Plan de Orquestación):**
```
Patrón: Jerárquico

Pasos:
1. **Manager**: Planificar y dividir tareas
2. **Agentes**: [analista, arquitecto] - Ejecución en paralelo
3. **Manager**: Consolidar resultados

Ventajas:
- Escalable
- Inteligente

Desventajas:
- Más complejo
```

---

## 🔍 Trazabilidad del Flujo

La aplicación incluye un sistema completo de **trazabilidad** que registra cada paso de la ejecución:

### Estados de Ejecución

```python
class EstadoEjecucion(Enum):
    INICIADO = "iniciado"
    ANALIZANDO_ENTRADA = "analizando_entrada"
    DETECTANDO_AREA = "detectando_area"
    IDENTIFICANDO_PROBLEMA = "identificando_problema"
    GENERANDO_SOLUCION = "generando_solucion"
    DISEÑANDO_ARQUITECTURA = "diseñando_arquitectura"
    ANALIZANDO_RIESGOS = "analizando_riesgos"
    GENERANDO_OUTPUT = "generando_output"
    COMPLETADO = "completado"
    ERROR = "error"
```

### Flujo de Ejecución

```
1. ✅ INICIADO - Inicialización del agente generador
2. ⏳ ANALIZANDO_ENTRADA - Analizando entrada del usuario
3. ⏳ DETECTANDO_AREA - Detectando área de negocio
4. ⏳ IDENTIFICANDO_PROBLEMA - Identificando problema específico
5. ⏳ GENERANDO_SOLUCION - Generando solución técnica
6. ⏳ DISEÑANDO_ARQUITECTURA - Diseñando arquitectura de alto nivel
7. ⏳ ANALIZANDO_RIESGOS - Analizando principales riesgos
8. ⏳ GENERANDO_OUTPUT - Generando propuesta final
9. ✅ COMPLETADO - Propuesta generada exitosamente
```

### Información Registrada

Por cada paso se registra:
- **Estado**: Identificador del paso
- **Detalle**: Descripción legible
- **Timestamp**: Cuándo ocurrió (ISO 8601)
- **Metadata**: Datos adicionales relevantes

### Métricas de Trazabilidad

```python
def obtener_resumen(self) -> Dict:
    return {
        "inicio": "2024-01-15T10:30:00",
        "fin": "2024-01-15T10:30:05",
        "duracion_ms": 5000,
        "total_pasos": 9,
        "total_errores": 0,
        "exitoso": True
    }
```

---

## 📁 Estructura de Archivos

```
generador/
├── app_streamlit.py       # Interfaz Streamlit principal
├── agent.py               # Lógica del agente + Trazabilidad
├── langchain_skills.py    # Skills de Arquitectura y Orquestación
├── templates.py           # Templates de propuestas por área
├── prompts.py             # Templates de prompts (reservado)
├── rules.md               # Reglas del proyecto
├── workflow.md            # Diagramas de flujo
├── README.md              # Este archivo
└── requirements.txt       # Dependencias Python
```

---

## 🚀 Ejecución

### Requisitos
```bash
pip install -r requirements.txt
```

### Ejecución Local
```bash
streamlit run app_streamlit.py
```

### Configuración
No requiere API key - usa **templates predefinidos** para generar propuestas.

---

## 📋 Áreas Disponibles

| Área | Descripción | Palabras Clave |
|------|-------------|----------------|
| **Fintech** | Pagos, banca, crédito | pagos, banco, transacciones, crédito |
| **App Móviles** | iOS, Android, multiplataforma | app, móvil, ios, android |
| **Blockchain** | Smart contracts, tokens, Web3 | blockchain, token, smart contract |
| **Arquitectura** | Microservicios, cloud, serverless | microservicios, docker, kubernetes |
| **Seguros** | Pólizas, reclamos, tarificación | póliza, reclamo, siniestro |
| **Médica** | EHR, telemedicina | paciente, historial clínico |
| **Telecomunicaciones** | OSS/BSS, redes | red, operador, facturación |
| **Transporte** | TMS, flotas | ruta, flota, entrega |
| **Almacenamiento** | WMS, inventario | bodega, inventario, picking |
| **Combustibles** | Estaciones, tanques | combustible, tanque, estación |

---

## 🔧 Desarrollo

### Reglas del Proyecto
Ver `rules.md` para:
- Configuración de modelos
- Validación de entrada
- Estructura de propuesta
- Manejo de errores

### Workflow
Ver `workflow.md` para:
- Diagramas de flujo de usuario
- Diagrama técnico LangChain
- Pasos de despliegue

---

## 📝 Licencia

MIT
