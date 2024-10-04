## AI Powered Chatbots: A Collection of AI-Powered Chatbots

This repository features multiple demo chatbots, each designed to handle a specific domain or task. These bots leverage natural language understanding and conversational AI to provide automated solutions that mimic human interaction.

### Bots Included
1. **DineBot**: An AI-powered restaurant assistant to help users browse menus, check prices, and place orders.
2. **HireBot**: A resume-querying assistant that helps tech leads find matching candidates by asking questions about resumes.
3. _(Add more bots here as we build them)_

### Features
- **Chainlit Integration**: All bots are built using the Chainlit framework for streamlined development and deployment of conversational applications.
- **OpenAI Models**: The bots use OpenAI's GPT models to process natural language queries and respond in a human-like manner.
- **LangChain**: LangChain is used for documents loading, splitting and embedding into Pinecone
- **Pinecone**: Pinecone is used to keep embedded documents and used later as a context
- **Expandable**: The repository will continue to grow with additional AI bots that demonstrate practical applications of conversational AI in various domains.
  

### Tech Stack
- Python 3.11
- Chainlit
- OpenAI
- LangChain
- Pinecone
- Docker

### Running a Chatbot

```
git clone git@github.com:BuildWithLal/ai-powered-chatbots.git
cd ai-powered-chatbot
```

To run `DineBot` (or any other bot), navigate to the respective bot's directory:

```
cd DineBot-AI-Powered-Restaurant-Assistant
```

```
docker compose up
```

```
user: admin
password: admin
```

visit http://localhost:8000 and keep botting...!
