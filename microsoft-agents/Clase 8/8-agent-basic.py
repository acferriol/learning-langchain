import random
import asyncio
from typing import Annotated
import logging
from agent_framework import tool
from agent_framework.openai import OpenAIChatClient
from pydantic import Field
from rich import print
from rich.logging import RichHandler


# Setup logging
handler = RichHandler(show_path=False, rich_tracebacks=True, show_level=False)
logging.basicConfig(
    level=logging.WARNING, handlers=[handler], force=True, format="%(message)s"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


client = OpenAIChatClient(
    base_url="http://localhost:11434/v1", api_key="nokeyneeded", model_id="llama3.2:3b"
)


@tool(approval_mode="never_require")
def get_weather(
    city: Annotated[str, Field(description="Nombre completo de la ciudad")],
) -> dict:
    """Devuelve datos meteorológicos para una ciudad: temperatura y descripción."""
    logger.info(f"Obteniendo el clima para {city}")
    if random.random() < 0.05:
        return {
            "temperature": 72,
            "description": "Soleado",
        }
    else:
        return {
            "temperature": 60,
            "description": "Lluvioso",
        }


agent = client.as_agent(
    name="WeatherAgent",
    instructions="Eres un agente informativo. Responde a las preguntas con alegría.",
    tools=[get_weather],
)


async def main():
    response = await agent.run("¿Cómo está el clima hoy en San Francisco?")
    print(response.text)


if __name__ == "__main__":
    asyncio.run(main())
