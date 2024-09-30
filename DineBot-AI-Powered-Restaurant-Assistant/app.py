import chainlit as cl
from src.llm import take_order


@cl.on_message
async def main(message: cl.Message):
    response = take_order(message.content)

    # Send a response back to the user
    await cl.Message(content=response).send()
