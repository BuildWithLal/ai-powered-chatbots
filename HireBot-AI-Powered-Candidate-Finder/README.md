## HireBot: AI-Powered Resume Assistant

HireBot is a sample chatbot built using Chainlit, LangChain, Pinecone, OpenAI and Embeddings that helps recruiters and tech lead to query resumes based on the uploaded resumes.

<br/>

![hirebot-final-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/fef47940-29ed-4123-888e-ba2abe5b7087)

<br/>

![hirebot-final-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/4c64db51-f0cd-4b9f-b06b-a6384e0a5cbf)



<br/>

### Key Features:

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
* OpenAI
* LiteralAI
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
