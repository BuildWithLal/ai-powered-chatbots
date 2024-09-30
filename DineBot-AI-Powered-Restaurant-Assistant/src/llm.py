from openai import OpenAI
from src.prompt import system_message


client = OpenAI()

messages = [
    {'role': 'system', 'content': system_message}
]

def take_order(message, model="gpt-4o-mini", temperature=0.5):

    messages.append(
        {'role': 'user', 'content': message}
    )

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    messages.append(
        {'role': 'assistant', 'content': response.choices[0].message.content}
    )

    return response.choices[0].message.content

