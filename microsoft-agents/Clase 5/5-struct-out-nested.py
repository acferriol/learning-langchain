import openai
from pydantic import BaseModel, Field


class Participant(BaseModel):
    name: str = Field(description="Nombre de la persona")
    job: str = Field(description="Trabajo")


class CalendarEvent(BaseModel):
    name: str = Field(description="Nombre del evento")
    date: str = Field(description="Fecha histórica")
    participants: list[Participant] = Field(description="Participantes")


MODEL_NAME = "llama3.2:3b"


client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

completion = client.chat.completions.parse(  # PARSE!
    model=MODEL_NAME,
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": "Extrae la información del evento",
        },
        {
            "role": "user",
            "content": "Alice la doctora y Bob el carpintero fueron a la feria de ciencias el domingo",
        },
    ],
    response_format=CalendarEvent,
)

message = completion.choices[0].message
if message.refusal:
    print(message.refusal)
else:
    event = message.parsed
    print(event)
    print(type(event))
