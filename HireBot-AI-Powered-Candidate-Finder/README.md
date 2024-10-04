### HireBot: AI-Powered Resume Assistant

HireBot is a sample chatbot built using Chainlit, LangChain, Pinecone, OpenAI and Embeddings that helps recruiters and tech lead to query resumes based on the uploaded resumes.

<br/>

![image](https://github.com/user-attachments/assets/f56e0ba7-07e1-489c-9108-0062e93cad43)


<br/>

#### Key Features:

* Upload Resumes: You can upload up to 5 PDF resumes in one chat.
* Ask Questions: Ask any questions related to the uploaded resumes to help you find the right candidate for a job.
* Supports login with Google and GitHub.

HireBot shows how to use tools like Chainlit, LangChain, Pinecone, OpenAI, and Embeddings to build chat applications for recruiters and hiring managers.

It demonstrates how to interact with the OpenAI GPT-4o-mini model through the OpenAI API.

Resumes are uploaded, broken into smaller chunks using LangChain, and then converted into embeddings. These embeddings are sent to OpenAI to handle your queries in context.

The chatbot will help you search for skills, candidates, experience levels, or even find the best match for a job based on the resumes you provide.


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
