### DineBot: AI-Powered Restaurant Assistant

DineBot is a sample chatbot built using Chainlit and OpenAI that simulates a restaurant assistant capable of helping users with menu browsing, item pricing, and placing orders. The chatbot provides a seamless and conversational interface to explore restaurant offerings and choose between cash or delivery options for their order.

<br/>

![untitled-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/5a81a9a1-84a7-4a36-9a47-67afe3e4c486)



<br/>

#### Key Features:
* Menu Browsing: Users can ask for available dishes, categories, and item details.
* Price Lookup: Quick and easy access to pricing for specific menu items.
* Order Assistance: Place an order for delivery or cash payment directly via the chatbot.
* Natural Conversations: The chatbot is trained to handle natural language queries, making interactions feel human-like and intuitive.
* DineBot demonstrates how Chainlit and OpenAI can be leveraged to create conversational applications for the restaurant industry, offering a practical use case of AI in customer service.

* It covers interacting with OpenAI `GPT-4o-mini` model using OpenAI API.
* The OpenAI system is trained with some sample restuarants including its menu and prices.
* This Chatbot will take order from customers by helping them choosing a restuarant and menu items along with prices.
* It will confirm order mode whether its a Delivery or Self-Pick order and COD or Pay-via-Card.
* It will ask for Delivery address also in case of COD.


### Tech Stack

* Chainlit
* OpenAI


### Run Chatbot
```
python -m venv .venv
```

```
source .venv/bin/activate
```

```
pip install -r requirements.txt
```

```
chainlit run app.py -w
```

visit http://localhost:8000 and Enjoy your MEAL!
