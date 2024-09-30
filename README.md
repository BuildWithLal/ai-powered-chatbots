### **AI Powered Chatbots: A Collection of AI-Powered Chatbots**

#### **Overview**
This repository features multiple demo chatbots, each designed to handle a specific domain or task. These bots leverage natural language understanding and conversational AI to provide automated solutions that mimic human interaction.

#### **Bots Included**
1. **DineBot**: An AI-powered restaurant assistant to help users browse menus, check prices, and place orders.
2. **HireBot**: A resume-querying assistant that helps tech leads find matching candidates by asking questions about resumes.
3. _(Add more bots here as we build them)_

#### **Features**
- **Chainlit Integration**: All bots are built using the Chainlit framework for streamlined development and deployment of conversational applications.
- **OpenAI Models**: The bots use OpenAI's GPT models to process natural language queries and respond in a human-like manner.
- **Expandable**: The repository will continue to grow with additional AI bots that demonstrate practical applications of conversational AI in various domains.
  

#### **Requirements**
- Python 3.10+
- Chainlit
- OpenAI API

#### **Installation**
1. Clone this repository:
   ```
   git clone git@github.com:BuildWithLal/ai-powered-chatbots.git
   cd ai-powered-chatbot
   ```

#### **Running a Chatbot**
To run **DineBot** (or any other bot), navigate to the respective bot's directory:

```
cd DineBot-AI-Powered-Restaurant-Assistant
```

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

visit http://localhost:8000 and keep botting...!
