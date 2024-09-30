#### Restaurant Chatbot using Chainlit and OpenAI

* This repo includes basic demo of Restaurant Chatbot using Chainlit and OpenAI.
* It covers interacting with OpenAI `GPT-3.5` model using OpenAI API.
* The OpenAI system is trained with some sample restuarants including its menu and prices.
* This Chatbot will take order from customers by helping them choosing a restuarant and menu items along with prices.
* It will confirm order mode whether its a Delivery or Self-Pick order and COD or Pay-via-Card.
* It will ask for Delivery address also in case of COD.

#### Tech Stack

* Chainlit
* OpenAI

#### Run Application
```
pip install -r requirements.txt
```

```
chainlit run app.py -w
```

visit http://localhost:8000 and Enjoy your MEAL!
