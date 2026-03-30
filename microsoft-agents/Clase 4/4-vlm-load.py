import openai
import base64

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

response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    n=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is pictured?.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": open_image_as_base64("sherl.jpg")},
                },
            ],
        }
    ],
)
print(response.choices[0].message.content)
