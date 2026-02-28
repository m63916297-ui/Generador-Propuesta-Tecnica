"""
Skills de LangChain para Arquitectura y Orquestación
Extiende el agente con capacidades avanzadas de LangChain
"""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class TipoArquitectura(Enum):
    """Tipos de arquitectura de microservicios"""

    MICROSERVICIOS = "microservicios"
    SERVERLESS = "serverless"
    EVENT_DRIVEN = "event_driven"
    MONOLITO = "monolito"
    HIBRIDA = "hibrida"


class PatronOrquestacion(Enum):
    """Patrones de orquestación de agentes"""

    SECUENCIAL = "secuencial"
    PARALELO = "paralelo"
    HIERARQUICO = "jerarquico"
    CONSUMER_PRODUCER = "consumer_producer"


@dataclass
class ComponenteArquitectura:
    """Define un componente de arquitectura"""

    nombre: str
    tipo: str
    descripcion: str
    tecnologias: List[str] = field(default_factory=list)
    dependencias: List[str] = field(default_factory=list)
    responsabilidad: str = ""


@dataclass
class SkillArquitectura:
    """Skill para generación de arquitecturas"""

    def generar_arquitectura_microservicios(
        self, contexto: str, servicios: List[str]
    ) -> Dict[str, ComponenteArquitectura]:
        """Genera arquitectura de microservicios"""

        componentes = {}

        componentes["api_gateway"] = ComponenteArquitectura(
            nombre="API Gateway",
            tipo="gateway",
            descripcion="Punto de entrada único para todas las APIs",
            tecnologias=["Kong", "AWS API Gateway", "Nginx"],
            responsabilidad="Routing, autenticación, rate limiting",
        )

        componentes["service_mesh"] = ComponenteArquitectura(
            nombre="Service Mesh",
            tipo="infraestructura",
            descripcion="Comunicación entre servicios",
            tecnologias=["Istio", "Linkerd", "Envoy"],
            responsabilidad="mTLS, observabilidad, balanceo",
        )

        for servicio in servicios:
            componentes[f"servicio_{servicio}"] = ComponenteArquitectura(
                nombre=f"Servicio {servicio.title()}",
                tipo="business",
                descripcion=f"Lógica de negocio para {servicio}",
                tecnologias=["Python/FastAPI", "Node.js/Express", "Go"],
                responsabilidad=f"Gestión de {servicio}",
            )

        componentes["base_datos"] = ComponenteArquitectura(
            nombre="Capa de Datos",
            tipo="persistencia",
            descripcion="Almacenamiento de datos",
            tecnologias=["PostgreSQL", "MongoDB", "Redis"],
            responsabilidad="Persistencia y caché",
        )

        componentes["mensajeria"] = ComponenteArquitectura(
            nombre="Sistema de Mensajería",
            tipo="async",
            descripcion="Comunicación asíncrona",
            tecnologias=["Kafka", "RabbitMQ", "AWS SQS"],
            responsabilidad="Eventos, colas, procesamiento async",
        )

        componentes["observabilidad"] = ComponenteArquitectura(
            nombre="Observabilidad",
            tipo="infraestructura",
            descripcion="Monitoreo y logging",
            tecnologias=["Prometheus", "Grafana", "ELK", "Jaeger"],
            responsabilidad="Métricas, logs, tracing",
        )

        return componentes

    def generar_arquitectura_serverless(
        self, contexto: str, funciones: List[str]
    ) -> Dict[str, ComponenteArquitectura]:
        """Genera arquitectura serverless"""

        componentes = {}

        componentes["http_gateway"] = ComponenteArquitectura(
            nombre="HTTP Gateway",
            tipo="gateway",
            descripcion="Trigger HTTP para funciones",
            tecnologias=["AWS API Gateway", "Cloud Functions", "Azure Functions"],
            responsabilidad="Enrutamiento HTTP",
        )

        componentes["storage"] = ComponenteArquitectura(
            nombre="Storage Layer",
            tipo="persistencia",
            descripcion="Almacenamiento de archivos y datos",
            tecnologias=["S3", "Azure Blob", "DynamoDB"],
            responsabilidad="Persistencia",
        )

        componentes["queue"] = ComponenteArquitectura(
            nombre="Message Queue",
            tipo="async",
            descripcion="Colas para procesamiento asíncrono",
            tecnologias=["AWS SQS", "Azure Queue", "Google Pub/Sub"],
            responsabilidad="Procesamiento async",
        )

        for fn in funciones:
            componentes[f"funcion_{fn}"] = ComponenteArquitectura(
                nombre=f"Función {fn.title()}",
                tipo="compute",
                descripcion=f"Función serverless para {fn}",
                tecnologias=["AWS Lambda", "Azure Functions", "Google Cloud Functions"],
                responsabilidad=f"Ejecutar lógica de {fn}",
            )

        componentes["cdn"] = ComponenteArquitectura(
            nombre="CDN",
            tipo="infraestructura",
            descripcion="Distribución de contenido estático",
            tecnologias=["CloudFront", "Azure CDN", "Cloud CDN"],
            responsabilidad="Entrega rápida de contenido",
        )

        return componentes

    def generar_diagrama_arquitectura(
        self, tipo: TipoArquitectura, contexto: str
    ) -> str:
        """Genera descripción de diagrama de arquitectura"""

        diagramas = {
            TipoArquitectura.MICROSERVICIOS: """
```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENTES                               │
│   (Web, Mobile, API Consumers)                               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      API GATEWAY                             │
│            (Kong / AWS API Gateway)                          │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Servicio A  │  │ Servicio B  │  │ Servicio C  │
│  (Core)     │  │  (Business) │  │  (Support)  │
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
   │ PostgreSQL│    │  Redis   │   │  Kafka   │
   │  (Data)  │    │  (Cache)  │   │ (Events) │
   └─────────┘    └──────────┘   └──────────┘
```
""",
            TipoArquitectura.SERVERLESS: """
```
┌─────────────────────────────────────────────────────────────┐
│                     USUARIOS                                 │
│         (Web, Mobile, IoT Devices)                          │
└────────────────────────┬────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    CDN / STATIC                              │
│              (CloudFront / S3)                             │
└────────────────────────┬────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  API GATEWAY                                 │
│           (Lambda Triggers)                                 │
└────┬────────────────┬────────────────┬─────────────────────┘
     │                │                │
     ▼                ▼                ▼
┌──────────┐    ┌──────────┐     ┌──────────┐
│ Lambda   │    │ Lambda   │     │ Lambda   │
│ Func A   │    │ Func B   │     │ Func C   │
└────┬─────┘    └────┬─────┘     └────┬─────┘
     │                │                │
     └────────┬───────┴────────┬───────┘
              │                │
              ▼                ▼
       ┌──────────┐     ┌──────────┐
       │ DynamoDB │     │    S3    │
       │  (NoSQL) │     │ (Files)  │
       └──────────┘     └──────────┘
```
""",
            TipoArquitectura.EVENT_DRIVEN: """
```
┌─────────────────────────────────────────────────────────────┐
│                      PRODUCTORES                             │
│   (API, Webhooks, IoT, Mobile)                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   KAFKA / RABBITMQ                           │
│              (Message Broker)                               │
└───────┬─────────────┬─────────────┬────────────────────────┘
        │             │             │
        ▼             ▼             ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Consumer   │ │  Consumer   │ │  Consumer   │
│  (Orders)   │ │  (Notif)    │ │  (Analytics)│
└──────┬──────┘ └──────┬──────┘ └──────┬──────┘
       │                │                │
       ▼                ▼                ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  PostgreSQL │ │   Redis     │ │  Snowflake  │
│  (OLTP)     │ │  (Cache)    │ │  (OLAP)     │
└─────────────┘ └─────────────┘ └─────────────┘
```
""",
        }

        return diagramas.get(tipo, "Diagrama no disponible")


@dataclass
class SkillOrquestacion:
    """Skill para orquestación de agentes"""

    def crear_agentes_especializados(
        self, areas: List[str]
    ) -> Dict[str, Dict[str, Any]]:
        """Crea configuración de agentes especializados"""

        configuraciones = {}

        agentes_base = {
            "analista": {
                "rol": "Analista de Requisitos",
                "responsabilidad": "Analizar y documentar necesidades",
                "prompt_base": "Eres un analista de negocio experto...",
            },
            "arquitecto": {
                "rol": "Arquitecto de Soluciones",
                "responsabilidad": "Diseñar arquitectura técnica",
                "prompt_base": "Eres un arquitecto de software senior...",
            },
            "desarrollador": {
                "rol": "Desarrollador Full Stack",
                "responsabilidad": "Implementar código",
                "prompt_base": "Eres un desarrollador experimentado...",
            },
            "qa": {
                "rol": "Ingeniero de Calidad",
                "responsabilidad": "Diseñar pruebas y validación",
                "prompt_base": "Eres un experto en testing...",
            },
            "devops": {
                "rol": "Ingeniero DevOps",
                "responsabilidad": "Infraestructura y despliegue",
                "prompt_base": "Eres un ingeniero DevOps experimentado...",
            },
        }

        for area in areas:
            configuraciones[area] = {
                "agentes": agentes_base,
                "flujo": self._determinar_flujo(area),
            }

        return configuraciones

    def _determinar_flujo(self, area: str) -> List[str]:
        """Determina el flujo de agentes según el área"""

        flujos = {
            "fintech": ["analista", "arquitecto", "devops", "qa"],
            "app_moviles": ["analista", "arquitecto", "desarrollador", "qa"],
            "blockchain": ["analista", "arquitecto", "desarrollador", "devops"],
            "default": ["analista", "arquitecto", "desarrollador", "qa", "devops"],
        }

        return flujos.get(area, flujos["default"])

    def crear_orquestacion_secuencial(
        self, agentes: List[str], input_inicial: str
    ) -> Dict[str, Any]:
        """Configura orquestación secuencial"""

        return {
            "tipo": PatronOrquestacion.SECUENCIAL,
            "agentes": agentes,
            "input_inicial": input_inicial,
            "descripcion": "Los agentes ejecutan en secuencia, pasando output como input al siguiente",
        }

    def crear_orquestacion_paralela(
        self, agentes: List[str], input_inicial: str
    ) -> Dict[str, Any]:
        """Configura orquestación paralela"""

        return {
            "tipo": PatronOrquestacion.PARALELO,
            "agentes": agentes,
            "input_inicial": input_inicial,
            "descripcion": "Todos los agentes reciben el mismo input y ejecutan concurrentemente",
        }

    def crear_orquestacion_hierarquica(
        self, manager: str, workers: List[str], input_inicial: str
    ) -> Dict[str, Any]:
        """Configura orquestación jerárquica"""

        return {
            "tipo": PatronOrquestacion.HIERARQUICO,
            "manager": manager,
            "workers": workers,
            "input_inicial": input_inicial,
            "descripcion": "Un agente manager coordina trabajadores especializados",
        }

    def generar_plan_ejecucion(
        self, necesidad: str, patron: PatronOrquestacion
    ) -> Dict[str, Any]:
        """Genera plan de ejecución basado en el patrón"""

        planes = {
            PatronOrquestacion.SECUENCIAL: {
                "pasos": [
                    {
                        "orden": 1,
                        "agente": "analista",
                        "descripcion": "Analizar necesidad",
                    },
                    {
                        "orden": 2,
                        "agente": "arquitecto",
                        "descripcion": "Diseñar solución",
                    },
                    {
                        "orden": 3,
                        "agente": "desarrollador",
                        "descripcion": "Implementar",
                    },
                    {"orden": 4, "agente": "qa", "descripcion": "Validar"},
                ],
                "ventajas": ["Orden claro", "Dependencias manejadas"],
                "desventajas": ["Tiempo total = suma de todos"],
            },
            PatronOrquestacion.PARALELO: {
                "pasos": [
                    {
                        "agentes": ["arquitecto", "devops", "qa"],
                        "descripcion": "Ejecución paralela",
                    }
                ],
                "ventajas": ["Más rápido", "Independencia"],
                "desventajas": ["Puede haber trabajo duplicado"],
            },
            PatronOrquestacion.HIERARQUICO: {
                "pasos": [
                    {
                        "orden": 1,
                        "agente": "manager",
                        "descripcion": "Planificar y dividir tareas",
                    },
                    {
                        "orden": 2,
                        "agentes": ["analista", "arquitecto"],
                        "descripcion": "Ejecutar en paralelo",
                    },
                    {
                        "orden": 3,
                        "agente": "manager",
                        "descripcion": "Consolidar resultados",
                    },
                ],
                "ventajas": ["Escalable", "Inteligente"],
                "desventajas": ["Más complejo"],
            },
        }

        return planes.get(patron, {})


@dataclass
class LangChainSkills:
    """Clase principal que integra ambos skills"""

    arquitectura: SkillArquitectura = field(default_factory=SkillArquitectura)
    orquestacion: SkillOrquestacion = field(default_factory=SkillOrquestacion)

    def generar_arquitectura_completa(
        self, tipo: TipoArquitectura, contexto: str, servicios: List[str]
    ) -> Dict[str, Any]:
        """Genera arquitectura completa con diagrama"""

        if tipo == TipoArquitectura.MICROSERVICIOS:
            componentes = self.arquitectura.generar_arquitectura_microservicios(
                contexto, servicios
            )
        elif tipo == TipoArquitectura.SERVERLESS:
            componentes = self.arquitectura.generar_arquitectura_serverless(
                contexto, servicios
            )
        else:
            componentes = {}

        diagrama = self.arquitectura.generar_diagrama_arquitectura(tipo, contexto)

        return {
            "tipo_arquitectura": tipo.value,
            "componentes": componentes,
            "diagrama": diagrama,
            "resumen": self._generar_resumen(componentes),
        }

    def _generar_resumen(self, componentes: Dict[str, ComponenteArquitectura]) -> str:
        """Genera resumen de la arquitectura"""

        resumen = "## Resumen de Componentes\n\n"

        for nombre, comp in componentes.items():
            resumen += f"### {comp.nombre}\n"
            resumen += f"- **Tipo**: {comp.tipo}\n"
            resumen += f"- **Descripción**: {comp.descripcion}\n"
            if comp.tecnologias:
                resumen += f"- **Tecnologías**: {', '.join(comp.tecnologias)}\n"
            if comp.responsabilidad:
                resumen += f"- **Responsabilidad**: {comp.responsabilidad}\n"
            resumen += "\n"

        return resumen

    def crear_agente_hibrido(
        self,
        necesidad: str,
        tipo_arquitectura: TipoArquitectura,
        patron_orquestacion: PatronOrquestacion,
    ) -> Dict[str, Any]:
        """Crea un agente híbrido con arquitectura y orquestación"""

        return {
            "necesidad": necesidad,
            "arquitectura": self.generar_arquitectura_completa(
                tipo_arquitectura, necesidad, []
            ),
            "orquestacion": self.orquestacion.generar_plan_ejecucion(
                necesidad, patron_orquestacion
            ),
        }


def crear_skills() -> LangChainSkills:
    """Factory function para crear skills"""
    return LangChainSkills()
