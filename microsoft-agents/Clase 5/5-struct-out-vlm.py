import openai
from pydantic import BaseModel, Field
from enum import Enum
import base64


class TypeCharacter(str, Enum):
    REAL = "Real"
    FICTICIO = "Ficticio"


class Character(BaseModel):
    name: str = Field(description="Nombre del personaje")
    tipo: TypeCharacter = Field(description="Tipo de personaje")


MODEL_NAME = "qwen3-vl:2b"


def open_image_as_base64(filename):
    with open(filename, "rb") as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        return f"data:image/jpg;base64,{image_base64}"


client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

completion = client.chat.completions.parse(
    model=MODEL_NAME,
    temperature=0,
    n=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Who is pictured?.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": open_image_as_base64("sherl.jpg")},
                },
            ],
        }
    ],
    response_format=Character,
)

message = completion.choices[0].message
if message.refusal:
    print(message.refusal)
else:
    print(message.parsed)
