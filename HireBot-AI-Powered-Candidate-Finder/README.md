## HireBot: AI-Powered Resume Assistant

HireBot is a sample chatbot built using Chainlit, LangChain, Pinecone, OpenAI and Embeddings that helps recruiters and tech leads to query resumes based on the uploaded resumes.

<br/>

<img src="https://github.com/user-attachments/assets/3847830c-5be0-4893-8a3f-9727ff683300" width="500" />
<img src="https://github.com/user-attachments/assets/e34cacdd-0c08-433f-ba03-adc4209e3a28" width="500" />
<br/>
<img src="https://github.com/user-attachments/assets/d48a357f-15bd-4081-8ace-d3621c043933" width="500" />
<img src="https://github.com/user-attachments/assets/99408b01-562c-4a07-a63b-ef4c3e77371a" width="500" />

<br/>

### Key Features:

* **Upload Resumes**: You can upload up to 5 PDF resumes in one chat.
* **Ask Questions**: Ask any questions related to the uploaded resumes to help you find the right candidate for a job.
* **Authentication**: Supports login with Google and GitHub.
* **Resume Existing Chat/Thread**
* **Rename Chat/Thread**
* **Preview PDF Resumes**: Preview resumes inside chat

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

visit http://localhost:8000 and Enjoy your recruiting!


### Queries
1. Could you provide me with a list of candidates who have extensive experience in Python?
2. Have any of these candidates also worked with React?
3. Which of these candidates would be a good fit for a full-stack Python/React role?
5. Could you please provide a list of the top 5 skills for each of the shortlisted candidates?
