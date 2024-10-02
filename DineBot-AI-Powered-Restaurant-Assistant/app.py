import chainlit as cl
from src.llm import take_order


@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")


import chainlit as cl

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Din Tai Fung",
            message="Known for its meticulous and delicious dumplings, Din Tai Fung offers a variety of Taiwanese dishes.",
            icon="/public/din-tai-fung.png",
            ),

        cl.Starter(
            label="Narisawa",
            message="Michelin-starred Narisawa fuses French techniques with traditional Japanese ingredients, focusing on seasonality and environmental sustainability.",
            icon="/public/narisawa.jpg",
            ),
        cl.Starter(
            label="Gaggan Anand",
            message="Gaggan Anand is renowned for his innovative twist on traditional Indian cuisine, often presented in a tasting menu format.",
            icon="/public/gaggan-anand.png",
            ),
        cl.Starter(
            label="Song Fang Zhai",
            message="A hidden gem known for authentic Chinese cuisine, particularly the Beijing specialties.",
            icon="/public/song-fang-zhai.jpg",
            )
        ]


@cl.on_message
async def main(message: cl.Message):
    response = take_order(message.content)

    # Send a response back to the user
    await cl.Message(content=response).send()


@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")

