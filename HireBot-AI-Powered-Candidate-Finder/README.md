### HireBot: AI-Powered Resume Assistant

HireBot is a sample chatbot built using Chainlit, LangChain, Pinecone, OpenAI and Embeddings that helps recruiters and tech lead to query resumes based on the uploaded resumes.

<br/>

![image](https://github.com/user-attachments/assets/f56e0ba7-07e1-489c-9108-0062e93cad43)


<br/>

#### Key Features:
* Upload PDF Resumes: User can upload up to 5 resumes in a single chat.
* Ask Questions: User can ask questions based on uploaded resumes to find the best candidate for a job.
* HireBot demonstrates how Chainlit, LangChain, Pinecone, OpenAI and Embeddings  can be leveraged to create conversational applications for the recruiters and tech leads.

* It covers interacting with OpenAI `GPT-4o-mini` model using OpenAI API.
* The resumes are uploaded, split and chunked using LangChain, created embeddings and passed to OpenAI for contextual queries.
* The ChatBot will answer any query based on the uploaded resumes to find out a skill, a candidate, experience levels or a best fit based on job
* Support Google and GitHub Login


### Tech Stack

* Python 3.11
* Chainlit
* LangChain
* Pinecone
* OpenAI API
* Docker


### Run Chatbot
```
docker compose up
```

```
user: admin
password: admin
```

visit http://localhost:8000 and Enjoy your MEAL!
