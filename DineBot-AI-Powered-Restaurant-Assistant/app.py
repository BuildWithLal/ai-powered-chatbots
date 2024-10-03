import os
import json
import chainlit as cl
from src.llm import take_order
from typing import Dict, Optional


@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")


@cl.set_starters
async def set_starters():
    restaurants = []
    with open(os.path.join('public', 'restaurants.json'), 'r') as f:
        restaurants = json.loads(f.read())
    
    starter_restaurants = []
    for restaurant in restaurants:
        starter_restaurants.append(
                cl.Starter(
                label=restaurant['label'],
                message=restaurant['message'],
                icon=restaurant['icon'],
            ))
    
    return starter_restaurants

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
def oauth_callback(provider_id: str, token: str, raw_user_data: Dict[str, str], default_user: cl.User) -> Optional[cl.User]:
  return default_user


@cl.on_message
async def main(message: cl.Message):
    await take_order(message)

@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")

