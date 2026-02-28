"""
Templates de Propuestas Técnicas por Área
Cada template incluye: problema, solución, arquitectura y riesgos
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TemplatePropuesta:
    """Estructura de un template de propuesta técnica"""

    area: str
    descripcion: str
    problema_base: str
    solucion_base: str
    arquitectura_base: str
    riesgos_base: List[str]
    tecnologias: List[str]
    palabras_clave: List[str]


TEMPLATES: Dict[str, TemplatePropuesta] = {
    "fintech": TemplatePropuesta(
        area="Fintech",
        descripcion="Soluciones financieras tecnológicas",
        problema_base="Los procesos financieros tradicionales son lentos, manuales y propensos a errores, lackedo de automatización y seguridad.",
        solucion_base="Plataforma financiera digital con procesamiento en tiempo real, cumplimiento normativo automático y APIs abiertas.",
        arquitectura_base="Arquitectura de microservicios con API Gateway, servicios de procesamiento de pagos, módulo de cumplimiento (KYC/AML), base de datos transaccional (PostgreSQL), caché (Redis), cola de mensajes (Kafka) para procesamiento asíncrono, y auditoría blockchain para trazabilidad.",
        riesgos_base=[
            "Cumplimiento regulatorio - Mitigación: Integración con servicios de compliance y auditoría continua",
            "Fraude financiero - Mitigación: Sistemas de detección de anomalías con ML y autenticación multifactor",
            "Disponibilidad 24/7 - Mitigación: Arquitectura redundante con auto-scaling y disaster recovery",
            "Seguridad de datos financieros - Mitigación: Encriptación en tránsito y reposo, tokenización de datos sensibles",
        ],
        tecnologias=[
            "Python/Django",
            "PostgreSQL",
            "Redis",
            "Kafka",
            "Kubernetes",
            "AWS/GCP",
            "Stripe API",
        ],
        palabras_clave=[
            "pagos",
            "banco",
            "transacciones",
            "crédito",
            "préstamo",
            "tarjeta",
            "banca",
            "finanzas",
            "criptomoneda",
        ],
    ),
    "app_moviles": TemplatePropuesta(
        area="Aplicaciones Móviles",
        descripcion="Desarrollo de apps iOS y Android",
        problema_base="Las aplicaciones existentes son lentas, no ofrecen experiencia de usuario óptima, y no se integran con otros sistemas empresariales.",
        solucion_base="Aplicación móvil nativa o multiplataforma con arquitectura moderna, sincronización offline, y backend escalable.",
        arquitectura_base="Frontend con Flutter/React Native para multiplataforma o Swift/Kotlin nativo. Backend como servicio (Firebase/AWS Amplify) o API REST/GraphQL propia. Sincronización offline con SQLite/Realm, notificaciones push (FCM), y analytics integrado.",
        riesgos_base=[
            "Fragmentación de dispositivos - Mitigación: Testing en múltiples dispositivos y versiones de OS",
            "Experiencia de usuario inconsistente - Mitigación: Diseño responsive y guías de estilo rigurosas",
            "Rendimiento en dispositivos de gama baja - Mitigación: Optimización de assets y código, lazy loading",
            "Actualizaciones frecuentes de OS - Mitigación: Actualizaciones proactivas del SDK y testing temprano",
        ],
        tecnologias=[
            "Flutter",
            "React Native",
            "Swift",
            "Kotlin",
            "Firebase",
            "GraphQL",
            "Realm",
        ],
        palabras_clave=[
            "app",
            "móvil",
            "ios",
            "android",
            "smartphone",
            "aplicación",
            "usuario",
            "interfaz",
        ],
    ),
    "blockchain": TemplatePropuesta(
        area="Blockchain",
        descripcion="Soluciones basadas en tecnología blockchain",
        problema_base="Falta de transparencia, trazabilidad insuficiente, costos elevados en intermediarios, y falta de confianza entre partes.",
        solucion_base="Plataforma blockchain para gestión de activos digitales, contratos inteligentes, y trazabilidad inmutable.",
        arquitectura_base="Red blockchain (Ethereum/Polygon/Hyperledger según caso de uso), smart contracts en Solidity/Rust, oráculos para datos externos (Chainlink), almacenamiento descentralizado (IPFS), wallet integration, y dashboard de análisis on-chain.",
        riesgos_base=[
            "Escalabilidad de la blockchain - Mitigación: Layer 2 solutions, sharding, o blockchain permissionada",
            "Regulación unclear - Mitigación: Asesoramiento legal especializado y arquitectura compliant",
            "Volatilidad de criptomonedas - Mitigación: Stablecoins o conversión a fiat inmediata",
            "Seguridad de smart contracts - Mitigación: Auditorías de código, bug bounties, y formales methods",
        ],
        tecnologias=[
            "Solidity",
            "Ethereum",
            "Polygon",
            "Hyperledger",
            "Web3.js",
            "IPFS",
            "Chainlink",
        ],
        palabras_clave=[
            "blockchain",
            "smart contract",
            "token",
            "criptomoneda",
            "descentralizado",
            "web3",
            "nft",
            "defi",
        ],
    ),
    "arquitectura": TemplatePropuesta(
        area="Arquitectura de Sistemas",
        descripcion="Diseño y modernización de infraestructura",
        problema_base="Sistemas monolíticos difíciles de mantener, acoplamiento fuerte, baja escalabilidad, y tiempos de despliegue lentos.",
        solucion_base="Modernización a arquitectura de microservicios o serverless con CI/CD, observabilidad completa, y infraestructura como código.",
        arquitectura_base="Contenedores con Docker y orquestación Kubernetes. API Gateway para routing, service mesh (Istio) para comunicación entre servicios, funciones serverless (AWS Lambda/Azure Functions) para cargas variables. Infraestructura con Terraform/Ansible, monitoreo con Prometheus/Grafana, logging centralizado (ELK), y tracing distribuido (Jaeger).",
        riesgos_base=[
            "Complejidad operativa - Mitigación: Documentación exhaustiva, training, y herramientas de gestión",
            "Latencia entre servicios - Mitigación: Comunicación sincrónica vs asíncrónica según caso, caching",
            "Gestión de datos distribuidos - Mitigación: Patrones de consistencia eventual, sagas para transacciones",
            "Curva de aprendizaje del equipo - Mitigación: Plan de capacitación y pair programming",
        ],
        tecnologias=[
            "Docker",
            "Kubernetes",
            "Terraform",
            "AWS",
            "Azure",
            "GCP",
            "Istio",
            "Prometheus",
        ],
        palabras_clave=[
            "microservicios",
            "serverless",
            "contenedores",
            "docker",
            "kubernetes",
            "cloud",
            "infraestructura",
            "despliegue",
        ],
    ),
    "seguros": TemplatePropuesta(
        area="Seguros",
        descripcion="Digitalización del sector asegurador",
        problema_base="Los procesos de cotización, suscripción y reclamos son manuales, lentos, y prone a errores humanos.",
        solucion_base="Plataforma de seguros digital con automatización de cotizaciones, evaluación de riesgos con IA, y procesamiento de reclamos automatizado.",
        arquitectura_base="Sistema de gestión de pólizas con motor de reglas de negocio (Drools), módulo de tarificación, integración con fuentes de datos externas (historial crediticio, dispositivos IoT), proceso de claims con workflow automatizado, y portal de autoservicio para clientes.",
        riesgos_base=[
            "Cumplimiento regulatorio de seguros - Mitigación: Motor de reglas validado por actuaristas, auditorías",
            "Fraude en reclamos - Mitigación: Detección de anomalías con ML, investigación basada en riesgo",
            "Integración con sistemas legacy - Mitigación: Capas de abstracción, migración gradual",
            "Pricing inadecuado - Mitigación: Modelos actuariales validados, revisión periódica",
        ],
        tecnologias=[
            "Java/Spring",
            "PostgreSQL",
            "Redis",
            "Drools",
            "Python/ML",
            "Camunda",
        ],
        palabras_clave=[
            "póliza",
            "reclamo",
            "siniestro",
            "cotización",
            "prima",
            "asegurado",
            "riesgo",
            "cobertura",
        ],
    ),
    "medica": TemplatePropuesta(
        area="Salud / Médica",
        descripcion="Digitalización del sector salud",
        problema_base="Fragmentación de información del paciente, procesos administrativos lentos, falta de interoperabilidad entre sistemas.",
        solucion_base="Sistema de gestión hospitalaria (HIS) integrado con EHR/EMR, telemedicina, y cumplimiento HIPAA.",
        arquitectura_base="EHR interoperable con estándares HL7 FHIR, sistema de citas y gestión de pacientes, módulo de telemedicina (WebRTC), integración con dispositivos médicos (IoT), motor de reglas clínicas, y portal de resultados para pacientes.",
        riesgos_base=[
            "Protección de datos de salud (HIPAA/GDPR) - Mitigación: Encriptación, controles de acceso, auditorías",
            "Interoperabilidad de sistemas - Mitigación: Estándares HL7 FHIR, APIs RESTful",
            "Disponibilidad crítica - Mitigación: Alta disponibilidad 99.99%, redundancia",
            "Errores médicos por software - Mitigación: Validaciones estrictas, testing clínico",
        ],
        tecnologias=[
            "HL7 FHIR",
            "Python/Django",
            "React",
            "PostgreSQL",
            "WebRTC",
            "IoMT",
        ],
        palabras_clave=[
            "paciente",
            "historial clínico",
            "cita",
            "médico",
            "diagnóstico",
            "receta",
            "hospital",
            "telemedicina",
        ],
    ),
    "telecomunicaciones": TemplatePropuesta(
        area="Telecomunicaciones",
        descripcion="Gestión de redes y servicios de telecom",
        problema_base="Gestión manual de red ineficiente, falta de visibilidad en tiempo real, y tiempos de resolución de fallas elevados.",
        solucion_base="Plataforma de gestión de red (OSS/BSS) con monitoreo en tiempo real, automatización de provisioning, y analytics predictivo.",
        arquitectura_base="Sistema de gestión de red (OSS) con SNMP/netconf monitoring, orchestration (ONAP), BSS para gestión de suscriptores y facturación, CRM integrado, mediation layer para conciliación de CDR, y dashboard de analytics en tiempo real.",
        riesgos_base=[
            "Disponibilidad de red crítica - Mitigación: Redundancia geográficamente distribuida, failover automático",
            "Volumen masivo de datos (CDRs, logs) - Mitigación: Procesamiento streaming, almacenamiento distribuido",
            "Integración con equipos legacy - Mitigación: Adaptadores, gradual migration",
            "Cumplimiento regulatorio de telecomunicaciones - Mitigación: Auditorías, logging inmutable",
        ],
        tecnologias=[
            "Java",
            "PostgreSQL",
            "Kafka",
            "SNMP",
            "ONAP",
            "Kubernetes",
            "Prometheus",
        ],
        palabras_clave=[
            "red",
            "operador",
            "servicio",
            "facturación",
            "cdr",
            "backhaul",
            "fibra",
            "5g",
        ],
    ),
    "transporte": TemplatePropuesta(
        area="Transporte y Logística",
        descripcion="Gestión de flotas y logística",
        problema_base="Rutas inefficientes, falta de visibilidad de carga, tiempos de entrega impredecibles, y costos operativos altos.",
        solucion_base="Plataforma de gestión de transporte (TMS) con optimización de rutas en tiempo real, tracking de flota, y visibilidad de extremo a extremo.",
        arquitectura_base="Módulo de optimización de rutas con algoritmos de ML, sistema de tracking GPS/IoT, gestión de flotas con conductor app, warehouse management integrado, visibilidad de carga en tiempo real, y analytics predictivo de demanda.",
        riesgos_base=[
            "Dependencia de datos de ubicación - Mitigación: Múltiples fuentes de GPS, offline capability",
            "Optimización de rutas complejas - Mitigación: Algoritmos probados, fallback a rutas经验adas",
            "Integración con operadores logísticos - Mitigación: APIs estándar, EDI",
            "Cambios last-mile - Mitigación: Flexibilidad en ventana de entrega, comunicación proactiva",
        ],
        tecnologias=[
            "Python",
            "PostgreSQL",
            "Redis",
            "GraphHopper",
            "AWS IoT",
            "React Native",
        ],
        palabras_clave=[
            "ruta",
            "flota",
            "camión",
            "entrega",
            "carga",
            "logística",
            "tracking",
            "conductor",
        ],
    ),
    "almacenamiento": TemplatePropuesta(
        area="Almacenamiento y Bodegaje",
        descripcion="Gestión de inventarios y almacenes",
        problema_base="Inventario desactualizado, ubicación ineficiente de productos, picking lento, y falta de trazabilidad.",
        solucion_base="Sistema de gestión de almacén (WMS) con código de barras/RFID, optimización de ubicaciones, y automatización de picking.",
        arquitectura_base="WMS con gestión de ubicaciones dinámicas, módulo de inbound/receiving, optimización de ubicaciones con ML, sistema de picking (wave/pick-to-light/voice), integración con robots AMR/AGV, y analytics de rotación de inventario.",
        riesgos_base=[
            "Inventario desincronizado - Mitigación: Contajes cíclicos, auditorías randomizadas",
            "Dependencia de hardware (scanners, RFID) - Mitigación: Redundancia, fallback manual",
            "Curva de aprendizaje del personal - Mitigación: Training intensivo, UI intuitiva",
            "Integración con ERP - Mitigación: Middleware, validación de datos bidireccional",
        ],
        tecnologias=["Java", "PostgreSQL", "RFID", "Barcode", "Kafka", "React", "IoT"],
        palabras_clave=[
            "bodega",
            "inventario",
            "picking",
            "ubicación",
            "producto",
            "stock",
            "recepción",
            "expedición",
        ],
    ),
    "combustibles": TemplatePropuesta(
        area="Combustibles y Energía",
        descripcion="Gestión de estaciones de servicio y distribución",
        problema_base="Control de inventario de combustibles ineficiente, falta de visibilidad de tanques, y procesos de conciliación manual.",
        solucion_base="Sistema de gestión de estaciones de servicio con monitoreo de tanques en tiempo real, automatización de pedidos, y conciliación automática.",
        arquitectura_base="Sistema de gestión de estaciones con módulo de tanques (ATG integration), control de dispensarios (fuel management), gestión de inventarios con forecasting, módulo de facturación y pos, integración con sistemas corporativos (ERP), y analytics de consumo.",
        riesgos_base=[
            "Fugas o robos de combustible - Mitigación: Monitoreo en tiempo real, alertas automáticas",
            "Cumplimiento ambiental - Mitigación: Monitorización de vapores, reportes regulatorios",
            "Dependencia de proveedores de combustible - Mitigación: Múltiples proveedores, contratos",
            "Fallos en hardware de medición - Mitigación: Calibración periódica, mantenimiento preventivo",
        ],
        tecnologias=["C#/.NET", "SQL Server", "IoT", "Modbus", "REST API", "Azure"],
        palabras_clave=[
            "combustible",
            "gasolina",
            "diésel",
            "tanque",
            "estación",
            "dispensario",
            "inventario",
            "bomba",
        ],
    ),
}


def detectar_area(necesidad: str) -> str:
    """
    Detecta el área más relevante basándose en palabras clave.
    Retorna el área identificada o 'general' como default.
    """
    necesidad_lower = necesidad.lower()

    mejor_area = "general"
    max_coincidencias = 0

    for area, template in TEMPLATES.items():
        coincidencias = sum(
            1 for palabra in template.palabras_clave if palabra in necesidad_lower
        )
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_area = area

    return mejor_area


def obtener_template(area: str) -> TemplatePropuesta:
    """Obtiene el template para un área específica"""
    return TEMPLATES.get(area, TEMPLATES["fintech"])


def listar_areas() -> List[str]:
    """Lista todas las áreas disponibles"""
    return list(TEMPLATES.keys())
