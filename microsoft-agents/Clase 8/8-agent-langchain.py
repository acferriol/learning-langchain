import logging
import os
import random
from datetime import datetime
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from rich import print
from rich.logging import RichHandler


# Setup logging
handler = RichHandler(show_path=False, rich_tracebacks=True, show_level=False)
logging.basicConfig(
    level=logging.WARNING, handlers=[handler], force=True, format="%(message)s"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


model = ChatOpenAI(
    base_url="http://localhost:11434/v1", api_key="nokeyneeded", model="llama3.2:3b"
)


@tool
def get_weather(city: str, date: str) -> dict:
    """Devuelve datos meteorológicos para una ciudad y fecha dadas."""
    logger.info(f"Obteniendo el clima para {city} en {date}")
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


@tool
def get_activities(city: str, date: str) -> list:
    """Devuelve una lista de actividades para una ciudad y fecha dadas."""
    logger.info(f"Obteniendo actividades para {city} en {date}")
    return [
        {"name": "Senderismo", "location": city},
        {"name": "Playa", "location": city},
        {"name": "Museo", "location": city},
    ]


@tool
def get_current_date() -> str:
    """Obtiene la fecha actual del sistema en formato YYYY-MM-DD."""
    logger.info("Obteniendo la fecha actual")
    return datetime.now().strftime("%Y-%m-%d")


agent = create_agent(
    model=model,
    system_prompt="Ayudas a las personas a planear su fin de semana y elegir las mejores actividades según el clima. Si una actividad sería desagradable con el clima previsto, no la sugieras. Incluye la fecha del fin de semana en tu respuesta.",
    tools=[get_weather, get_activities, get_current_date],
)


def main():
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Hola, ¿qué puedo hacer este fin de semana en San Francisco?",
                }
            ]
        }
    )
    latest_message = response["messages"][-1]
    print(latest_message.content)


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    main()
