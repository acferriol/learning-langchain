import openai
from pydantic import BaseModel


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


MODEL_NAME = "llama3.2:3b"


client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

completion = client.chat.completions.parse(  # PARSE!
    model=MODEL_NAME,
    temperature=0.2,
    messages=[
        {
            "role": "system",
            "content": "Extrae la información del evento",
        },
        {
            "role": "user",
            "content": "Alice y Bob van a la feria de ciencias el domingo",
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
