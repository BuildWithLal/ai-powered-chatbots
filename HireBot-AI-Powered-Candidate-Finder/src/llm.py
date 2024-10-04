import chainlit as cl
from openai import AsyncOpenAI

from src.prompt import system_message


client = AsyncOpenAI()

messages = [
    {'role': 'system', 'content': system_message}
]

async def take_order(message: cl.Message, model="gpt-4o-mini", temperature=0.5):

    messages.append(
        {'role': 'user', 'content': message.content}
    )

    message = cl.Message(content="")

    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True
    )

    async for part in response:
        if token := part.choices[0].delta.content or "":
            await message.stream_token(token)

    messages.append(
        {'role': 'assistant', 'content': message.content}
    )

    await message.update()

