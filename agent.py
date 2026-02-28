import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from prompts import PROMPT


class GeneradorPropuestas:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.7):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "La variable de entorno OPENAI_API_KEY no está configurada"
            )

        self.llm = ChatOpenAI(
            model_name=model_name, temperature=temperature, api_key=api_key
        )

        self.chain = LLMChain(llm=self.llm, prompt=PROMPT, verbose=False)

    def generar_propuesta(self, necesidad_negocio: str) -> str:
        if not necesidad_negocio or len(necesidad_negocio.strip()) < 10:
            raise ValueError(
                "La descripción de la necesidad debe tener al menos 10 caracteres"
            )

        resultado = self.chain.run(necesidad_negocio=necesidad_negocio)
        return resultado

    def generar_propuesta_con_historial(
        self, necesidad_negocio: str, historial: list[str] | None = None
    ) -> str:
        if historial is None:
            return self.generar_propuesta(necesidad_negocio)

        contexto = "\n".join(
            [f"Iteración {i + 1}: {h}" for i, h in enumerate(historial)]
        )
        necesidad_completa = f"{contexto}\n\nNecesidad actual: {necesidad_negocio}"

        return self.generar_propuesta(necesidad_completa)


def crear_agente(
    model_name: str = "gpt-4o-mini", temperature: float = 0.7
) -> GeneradorPropuestas:
    return GeneradorPropuestas(model_name=model_name, temperature=temperature)
