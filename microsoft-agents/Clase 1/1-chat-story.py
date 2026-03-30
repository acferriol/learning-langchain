import openai



if __name__=='__main__':
    
    client= openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",
    )

    MODEL_NAME = "llama3.2:3b"

    messages=[
           {"role": "system", "content": "I am a TA helping with Python questions for Berkeley CS 61A."},
        ]

    while True:
        question= input("\nYour question: ")
        messages.append({"role": "user", "content": question})
        response= client.chat.completions.create(
            #stream=True,
            model=MODEL_NAME,
            messages=messages
        )
        # for event in response:
        #     print(event.choices[0].delta.content, end="", flush=True)
        bot_response= response.choices[0].message.content
        messages.append({"role": "assistant", "content": bot_response})
        print(bot_response)
        


    