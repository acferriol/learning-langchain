import os

import azure.identity
import rich
from azure.ai.evaluation import (
    AzureOpenAIModelConfiguration,
    GroundednessEvaluator,
    OpenAIModelConfiguration,
)
from promptflow.client import load_flow

model_config: OpenAIModelConfiguration = {
    "api_key": "",
    "base_url": "http://localhost:11434/v1",
    "model": "llama3.2:3b",
    "type": "openai",
}

query = "Dada la especificación del producto para la Silla de Comedor de Contoso Home Furnishings, proporciona una descripción de marketing atractiva."
response = "Una silla de comedor elegante y cómoda que complementará cualquier decoración. Con un diseño moderno y materiales de alta calidad, esta silla es perfecta para disfrutar de tus comidas en familia o con amigos. Su estructura robusta garantiza durabilidad, mientras que su asiento acolchado ofrece una experiencia de confort excepcional. ¡Haz que tus momentos en la mesa sean aún más especiales con esta hermosa silla de Contoso Home Furnishings!"

friendliness_eval = load_flow(
    source="friend.prompty", model={"configuration": model_config}
)
friendliness_score = friendliness_eval(query=query, response=response)

rich.print(friendliness_score)
