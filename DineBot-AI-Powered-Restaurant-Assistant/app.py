import chainlit as cl
from src.llm import take_order
from typing import Dict, Optional


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


@cl.password_auth_callback
def auth():
    return cl.User(identifier="test")

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None
    

@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user

@cl.on_message
async def main(message: cl.Message):
    response = take_order(message.content)

    # Send a response back to the user
    await cl.Message(content=response).send()


@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")

