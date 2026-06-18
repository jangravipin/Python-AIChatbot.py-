from openai import OpenAI

key = "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"

messages = []

client = OpenAI(api_key=key)

def completion(user_message):
    global messages

    messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    assistant_message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }

    messages.append(assistant_message)

    print(f"Alexa: {assistant_message['content']}")

if __name__ == "__main__":
    print("Alexa: Hi, I am Alexa, how may I help you?\n")

    while True:
        user_question = input("User: ")
        completion(user_question)