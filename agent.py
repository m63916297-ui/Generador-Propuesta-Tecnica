"""
Agente Generador de Propuestas Técnicas
Sin necesidad de API key externo - usa templates predefinidos
"""

import re
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from templates import TEMPLATES, detectar_area, listar_areas, obtener_template


class EstadoEjecucion(Enum):
    """Estados posibles durante la ejecución del agente"""

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


@dataclass
class Trazabilidad:
    """Clase para registrar la trazabilidad de la ejecución"""

    pasos: List[Dict[str, Any]] = field(default_factory=list)
    errores: List[Dict[str, str]] = field(default_factory=list)
    inicio: Optional[datetime] = None
    fin: Optional[datetime] = None
    duracion_ms: int = 0

    def agregar_paso(
        self, estado: EstadoEjecucion, detalle: str, metadata: Optional[Dict] = None
    ):
        """Registra un paso en la trazabilidad"""
        self.pasos.append(
            {
                "estado": estado.value,
                "detalle": detalle,
                "timestamp": datetime.now().isoformat(),
                "metadata": metadata or {},
            }
        )

    def agregar_error(self, tipo: str, mensaje: str, contexto: str = ""):
        """Registra un error"""
        self.errores.append(
            {
                "tipo": tipo,
                "mensaje": mensaje,
                "contexto": contexto,
                "timestamp": datetime.now().isoformat(),
            }
        )

    def iniciar(self):
        """Marca el inicio de la ejecución"""
        self.inicio = datetime.now()

    def finalizar(self):
        """Marca el fin de la ejecución"""
        self.fin = datetime.now()
        if self.inicio:
            self.duracion_ms = int((self.fin - self.inicio).total_seconds() * 1000)

    def obtener_resumen(self) -> Dict[str, Any]:
        """Obtiene un resumen de la ejecución"""
        return {
            "inicio": self.inicio.isoformat() if self.inicio else None,
            "fin": self.fin.isoformat() if self.fin else None,
            "duracion_ms": self.duracion_ms,
            "total_pasos": len(self.pasos),
            "total_errores": len(self.errores),
            "exitoso": len(self.errores) == 0,
        }


@dataclass
class ResultadoPropuesta:
    """Resultado de la generación de propuesta"""

    propuesta: str
    area_detectada: str
    inputs: Dict[str, Any]
    outputs: Dict[str, Any]
    exitoso: bool
    trazabilidad: Optional[Trazabilidad] = None
    error: Optional[str] = None


class GeneradorPropuestas:
    """
    Generador de Propuestas Técnicas sin API key.
    Usa templates predefinidos por área con personalización basada en la entrada.
    """

    def __init__(self):
        self.templates = TEMPLATES
        self.areas = listar_areas()

    def _extraer_palabras_clave(self, necesidad: str) -> List[str]:
        """Extrae palabras clave de la necesidad"""
        stop_words = {
            "el",
            "la",
            "los",
            "las",
            "un",
            "una",
            "de",
            "del",
            "en",
            "con",
            "para",
            "por",
            "que",
            "y",
            "o",
            "a",
            "se",
            "son",
            "es",
            "esta",
            "esto",
            "necesitamos",
            "necesito",
            "queremos",
        }
        palabras = re.findall(r"\b[a-záéíóúñ]{4,}\b", necesidad.lower())
        return [p for p in palabras if p not in stop_words]

    def _identificar_problema(self, necesidad: str, template) -> str:
        """
        Identifica el problema específico basándose en la necesidad.
        Combina el problema base del template con la necesidad específica.
        """
        palabras_clave = self._extraer_palabras_clave(necesidad)

        problema = template.problema_base + "\n\n"
        problema += f"**Necesidad específica identificada:** {necesidad}\n\n"
        problema += f"**Palabras clave detectadas:** {', '.join(palabras_clave[:10])}"

        return problema

    def _generar_solucion(self, necesidad: str, template) -> str:
        """Genera la solución técnica personalizada"""
        palabras_clave = self._extraer_palabras_clave(necesidad)

        solucion = template.solucion_base + "\n\n"
        solucion += "**Componentes específicos sugeridos:**\n"

        componentes = {
            "fintech": "- Procesador de pagos en tiempo real\n- Módulo de KYC/AML\n- Dashboard de análisis financiero",
            "app_moviles": "- App móvil nativa/multiplataforma\n- Backend API REST/GraphQL\n- Sistema de notificaciones push",
            "blockchain": "- Smart contracts para automatización\n- Sistema de tokens\n- Oráculos para datos externos",
            "arquitectura": "- Contenedores y orquestación\n- API Gateway\n- Sistema de observabilidad",
            "seguros": "- Motor de tarificación\n- Workflow de reclamos\n- Portal de autoservicio",
            "medica": "- Sistema de historial clínico (EHR)\n- Módulo de telemedicina\n- Portal de pacientes",
            "telecomunicaciones": "- OSS/BSS integrado\n- Sistema de provisioning\n- Analytics en tiempo real",
            "transporte": "- TMS con optimización de rutas\n- Tracking GPS\n- Gestión de flotas",
            "almacenamiento": "- WMS con RFID\n- Optimización de ubicaciones\n- Sistema de picking automatizado",
            "combustibles": "- Monitoreo de tanques (ATG)\n- Control de dispensarios\n- Gestión de inventario",
        }

        solucion += componentes.get(template.area, "- Módulos personalizados")

        return solucion

    def _disenar_arquitectura(self, necesidad: str, template) -> str:
        """Diseña la arquitectura de alto nivel"""
        return template.arquitectura_base

    def _analizar_riesgos(self, necesidad: str, template) -> List[str]:
        """Analiza los riesgos específicos"""
        palabras_clave = self._extraer_palabras_clave(necesidad)

        riesgos = template.riesgos_base.copy()

        riesgos_personalizados = {
            "fintech": [
                "Adaptación al mercado crypto - Mitigación: Monitoreo de tendencias y regulación",
            ],
            "app_moviles": [
                "Retención de usuarios - Mitigación: Analytics y engagement features",
            ],
            "blockchain": [
                "Adopción por usuarios - Mitigación: UX simplificada y onboarding guiado",
            ],
        }

        if template.area in riesgos_personalizados:
            riesgos.extend(riesgos_personalizados[template.area])

        return riesgos

    def generar_propuesta(
        self,
        necesidad: str,
        area_especifica: Optional[str] = None,
        incluir_trazabilidad: bool = True,
    ) -> ResultadoPropuesta:
        """
        Genera una propuesta técnica estructurada.

        Args:
            necesidad: Descripción corta de la necesidad de negocio
            area_especifica: Fuerza un área específica (opcional)
            incluir_trazabilidad: Si incluye trazabilidad en el resultado

        Returns:
            ResultadoPropuesta con la propuesta generada
        """
        trazabilidad = Trazabilidad()

        try:
            trazabilidad.iniciar()
            trazabilidad.agregar_paso(
                EstadoEjecucion.INICIADO,
                "Inicialización del agente generador",
                {"necesidad_length": len(necesidad)},
            )

            if not necesidad or len(necesidad.strip()) < 10:
                raise ValueError("La descripción debe tener al menos 10 caracteres")

            trazabilidad.agregar_paso(
                EstadoEjecucion.ANALIZANDO_ENTRADA,
                "Analizando entrada del usuario",
                {"necesidad": necesidad[:100] + "..."},
            )

            trazabilidad.agregar_paso(
                EstadoEjecucion.DETECTANDO_AREA, "Detectando área de negocio", {}
            )

            if area_especifica and area_especifica in self.areas:
                area = area_especifica
                trazabilidad.agregar_paso(
                    EstadoEjecucion.DETECTANDO_AREA,
                    f"Área forzada por el usuario: {area}",
                    {"area": area},
                )
            else:
                area = detectar_area(necesidad)
                trazabilidad.agregar_paso(
                    EstadoEjecucion.DETECTANDO_AREA,
                    f"Área detectada automáticamente: {area}",
                    {"area": area},
                )

            template = obtener_template(area)

            trazabilidad.agregar_paso(
                EstadoEjecucion.IDENTIFICANDO_PROBLEMA,
                "Identificando problema específico",
                {"template": area},
            )
            problema = self._identificar_problema(necesidad, template)

            trazabilidad.agregar_paso(
                EstadoEjecucion.GENERANDO_SOLUCION, "Generando solución técnica", {}
            )
            solucion = self._generar_solucion(necesidad, template)

            trazabilidad.agregar_paso(
                EstadoEjecucion.DISEÑANDO_ARQUITECTURA,
                "Diseñando arquitectura de alto nivel",
                {},
            )
            arquitectura = self._disenar_arquitectura(necesidad, template)

            trazabilidad.agregar_paso(
                EstadoEjecucion.ANALIZANDO_RIESGOS, "Analizando principales riesgos", {}
            )
            riesgos = self._analizar_riesgos(necesidad, template)

            trazabilidad.agregar_paso(
                EstadoEjecucion.GENERANDO_OUTPUT, "Generando propuesta final", {}
            )

            propuesta_final = self._formatear_propuesta(
                problema, solucion, arquitectura, riesgos, template
            )

            trazabilidad.finalizar()
            trazabilidad.agregar_paso(
                EstadoEjecucion.COMPLETADO,
                "Propuesta generada exitosamente",
                {"duracion_ms": trazabilidad.duracion_ms},
            )

            return ResultadoPropuesta(
                propuesta=propuesta_final,
                area_detectada=area,
                inputs={"necesidad": necesidad, "area_especifica": area_especifica},
                outputs={
                    "problema": problema,
                    "solucion": solucion,
                    "arquitectura": arquitectura,
                    "riesgos": riesgos,
                    "tecnologias": template.tecnologias,
                },
                trazabilidad=trazabilidad if incluir_trazabilidad else None,
                exitoso=True,
            )

        except ValueError as e:
            trazabilidad.finalizar()
            trazabilidad.agregar_error("ValueError", str(e), "Validación de entrada")
            return ResultadoPropuesta(
                propuesta="",
                area_detectada="",
                inputs={"necesidad": necesidad},
                outputs={},
                trazabilidad=trazabilidad,
                exitoso=False,
                error=str(e),
            )
        except Exception as e:
            trazabilidad.finalizar()
            trazabilidad.agregar_error("Exception", str(e), "Ejecución del agente")
            return ResultadoPropuesta(
                propuesta="",
                area_detectada="",
                inputs={"necesidad": necesidad},
                outputs={},
                trazabilidad=trazabilidad,
                exitoso=False,
                error=f"Error inesperado: {str(e)}",
            )

    def _formatear_propuesta(
        self,
        problema: str,
        solucion: str,
        arquitectura: str,
        riesgos: List[str],
        template,
    ) -> str:
        """Formatea la propuesta en markdown estructurado"""
        return f"""# PROPUESTA TÉCNICA

## Área: {template.area}

---

## 1. PROBLEMA IDENTIFICADO

{problema}

---

## 2. SOLUCIÓN TÉCNICA SUGERIDA

{solucion}

---

## 3. ARQUITECTURA GENERAL (ALTO NIVEL)

{arquitectura}

### Tecnologías Recomendadas
{", ".join(template.tecnologias)}

---

## 4. PRINCIPALES RIESGOS

{chr(10).join(f"- **{riesgo.split(' - ')[0]}**: {riesgo.split(' - ')[1] if ' - ' in riesgo else ''}" for riesgo in riesgos)}

---

*Propuesta generada automáticamente - Revisar y personalizar según requisitos específicos*
"""


def crear_agente() -> GeneradorPropuestas:
    """Factory function para crear el agente"""
    return GeneradorPropuestas()


def listar_areas_disponibles() -> List[str]:
    """Lista las áreas disponibles"""
    return listar_areas()
