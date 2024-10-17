## DineBot: AI-Powered Restaurant Assistant

DineBot is a sample chatbot built using Chainlit and OpenAI that simulates a restaurant assistant capable of helping users with menu browsing, item pricing, and placing orders. The chatbot provides a seamless and conversational interface to explore restaurant offerings and choose between cash or delivery options for their order.

<br/>

![untitled-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/5a81a9a1-84a7-4a36-9a47-67afe3e4c486)



<br/>

### Key Features:
* Menu Browsing: Users can ask for available dishes, categories, and item details.
* Price Lookup: Quick and easy access to pricing for specific menu items.
* Order Assistance: Place an order for delivery or cash payment directly via the chatbot.
* DineBot demonstrates how Chainlit and OpenAI can be leveraged to create conversational applications for the restaurant industry, offering a practical use case of AI in customer service.

* It covers interacting with OpenAI `GPT-4o-mini` model using OpenAI API.
* The OpenAI system is trained with some sample restuarants including its menu and prices.
* This Chatbot will take order from customers by helping them choosing a restuarant and menu items along with prices.
* It will confirm order mode whether its a Delivery or Self-Pick order and COD or Pay-via-Card.
* It will ask for Delivery address also in case of COD.
* Support Google and GitHub Login


### Tech Stack

* Python 3.11
* Chainlit
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


Here’s a detailed breakdown of the **Medical Information Bot (LangChain + Hugging Face Transformers)** project, covering the domain, use cases, and tech stack:

---

### **1. Domain Overview:**

The **Medical Information Bot** operates within the healthcare domain, focusing on assisting users in understanding medical reports, conditions, or general healthcare inquiries. This bot uses domain-specific AI models to handle medical terminology, interpret clinical documents, and provide informed responses based on pre-trained medical language models. 

**Key Domain Focus:**
- **Healthcare & Medical Reports:** Understanding medical language, interpreting reports (e.g., lab results, radiology reports), and providing relevant information to users.
- **Medical Queries:** Answering questions about diseases, conditions, symptoms, medications, or treatments using AI models trained in the healthcare domain.

This bot is not intended to replace medical professionals but to provide informative insights from reliable data sources and pre-trained medical models.

---

### **2. Use Cases:**

- **Medical Report Upload & Analysis:** Users can upload their medical reports (e.g., lab results, prescriptions, discharge summaries) in formats like PDFs or images. The bot will analyze these reports using AI to explain complex medical terms and suggest potential next steps or clarify results.
  
  **Example:** A user uploads their blood test report, and the bot can explain what terms like "hemoglobin," "platelets," or "LDL cholesterol" mean, along with potential health implications based on provided ranges.

- **Medical Condition Queries:** Users can ask questions about specific diseases or medical conditions. The bot, powered by Hugging Face’s pre-trained models, retrieves relevant information from embedded documents or models fine-tuned on medical data.

  **Example:** A user may ask, “What are the symptoms of diabetes?” or “How is hypertension treated?” and receive a response based on pre-trained medical knowledge.

- **Search Through Medical Data:** The bot can search through uploaded medical documents or a database of medical literature to find relevant information. This allows healthcare providers or patients to gain insights from medical documents without going through the entire document themselves.

  **Example:** The bot can sift through a collection of uploaded clinical studies to find sections relevant to a user's query, such as treatments for a specific type of cancer.

- **Pre-trained Model Assistance:** By leveraging Hugging Face’s pre-trained models in the medical field (such as BioBERT, ClinicalBERT, or SciBERT), the bot can assist with scientific literature, drug interactions, and treatment plans.

  **Example:** A healthcare professional uploads journal articles, and the bot helps summarize research on emerging treatments for heart disease.

---

### **3. Tech Stack:**

- **Chainlit**: The frontend interface for the chatbot where users can interact. Chainlit handles the conversation logic, displaying responses and managing interactions like file uploads (medical reports) and user questions. It is used to orchestrate the flow of chat-based interactions in a streamlined manner.

- **Hugging Face Transformers**: The bot uses pre-trained models from Hugging Face, specifically focused on the healthcare and medical domains. Examples of these models are:
  - **BioBERT**: Fine-tuned on biomedical literature.
  - **ClinicalBERT**: Tailored for clinical text analysis.
  - **SciBERT**: For scientific and medical literature.
  These models help in understanding and generating domain-specific language, allowing the bot to interpret medical content accurately and answer questions based on healthcare data.

- **LangChain**: Used for document splitting and managing larger texts (e.g., medical reports or journal articles). LangChain breaks down large medical documents into smaller chunks and processes them, making it easier to handle and retrieve information for contextual queries.

- **Pinecone**: This is the vector database used to store the embeddings of medical documents. When a query is made, Pinecone helps by searching through the embeddings for the most relevant sections of the documents. The embeddings are generated from the medical reports and questions using Hugging Face’s pre-trained models. Pinecone makes the search process efficient by focusing on the most contextually relevant parts of documents.

- **OpenAI API (Optional)**: While the focus is on Hugging Face models for medical domain specificity, OpenAI’s GPT models could also be used to handle more general medical queries or tasks where Hugging Face models don’t fit. OpenAI’s powerful language models can complement the bot by providing conversational responses to broader queries.

- **Docker**: Used for containerization, Docker simplifies the deployment of the bot across different environments, making it easier to run the chatbot locally or on cloud infrastructure.

---

### **4. Workflow:**

1. **User Interaction:** Users initiate a conversation with the bot via Chainlit. They can either upload medical documents (PDFs or images) or ask direct questions about medical conditions.
   
2. **Document Splitting & Processing (LangChain):** If a medical report is uploaded, LangChain breaks it down into smaller sections for easier analysis. These smaller sections are then processed for embeddings.
   
3. **Model Inference (Hugging Face Transformers):** The chatbot leverages the pre-trained medical models from Hugging Face to interpret the uploaded data or answer medical queries. The embeddings are generated for the document chunks, and relevant parts of the documents are identified.

4. **Searching for Relevant Information (Pinecone):** If the user asks a question related to the uploaded documents, the embeddings are used to find the most relevant sections in Pinecone’s vector database. This allows the bot to provide context-specific answers based on the user's query.

5. **Response Generation:** The bot generates a response, either by explaining medical terminology, summarizing sections of a medical report, or answering questions related to the user's input.

---

### **5. Potential Enhancements:**

- **Fine-tuning for Specific Use Cases:** By further fine-tuning the models on more specific medical datasets (e.g., cardiology, oncology), the chatbot can become more specialized for certain medical fields.
- **Voice Interaction Integration (Whisper + ElevenLabs):** To make the bot more accessible, voice interaction could be integrated using Whisper for speech-to-text and ElevenLabs for text-to-speech, enabling voice queries and responses.
- **Multi-language Support:** For global applications, additional language support could be added using models trained on multilingual medical corpora.

---

This chatbot serves as an advanced demonstration of how AI models tailored to the medical domain can assist users in processing complex medical information and answering healthcare-related queries. It highlights the potential of leveraging AI to democratize access to medical insights, making it a valuable tool for both healthcare professionals and patients.