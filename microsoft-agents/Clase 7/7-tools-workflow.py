import openai
import json

client = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="nokeyneeded")
MODEL_NAME = "llama3.2:3b"


def lookup_weather(city_name=None, zip_code=None):
    print(f"Lookingup weather for {city_name or zip_code}...")
    return "Sunny, high of 70°F"


tools = [
    {
        "type": "function",
        "function": {
            "name": "lookup_weather",
            "description": "Busca el clima para un nombre de ciudad o código postal dado.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city_name": {
                        "type": "string",
                        "description": "El nombre de la ciudad",
                    },
                    "zip_code": {
                        "type": "string",
                        "description": "El código postal",
                    },
                },
                "additionalProperties": False,
            },
        },
    }
]

messages = [
    {"role": "system", "content": "Eres un chatbot de clima."},
    {"role": "user", "content": "Está soleado en Berkeley CA?"},
]
response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

print(f"Respuesta de {MODEL_NAME}: \n")

if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    print(tool_call.function.name)
    print(tool_call.function.arguments)
else:
    print(response.choices[0].message.content)


if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    if function_name == "lookup_weather":
        messages.append(response.choices[0].message)
        result = lookup_weather(**arguments)
        messages.append(
            {"role": "tool", "tool_call_id": tool_call.id, "content": str(result)}
        )
        response = client.chat.completions.create(
            model=MODEL_NAME, messages=messages, tools=tools
        )
        print(response.choices[0].message.content)
