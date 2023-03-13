import openai

openai.api_key = "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"

while True:

    prompt = input("\n ¿Cual es tu pregunta?")

    if prompt == "Salir":
        break

    pregunta = openai.Completion.create(engine="text-davinci-003",
                        prompt = prompt,
                        max_tokens = 2048,
                        )

    print(pregunta.choices[0].text)



