## HealthInsight - AI Powered Medical Assistant

The **Medical Bot** operates within the healthcare domain, focusing on assisting users in understanding medical reports, conditions, or general healthcare inquiries. This bot uses domain-specific AI models to handle medical terminology, interpret clinical documents, and provide informed responses based on pre-trained medical language models. 

*This bot is not intended to replace medical professionals but to provide informative insights from reliable data sources and pre-trained medical models.*

### Key Features
- **Medical Report Upload & Analysis:** Users can upload their medical reports (e.g., lab results, prescriptions, discharge summaries) in formats like PDFs or images. The bot will analyze these reports using AI to explain complex medical terms and suggest potential next steps or clarify results.
- **Medical Queries:** Answering questions about diseases, conditions, symptoms, medications, or treatments using AI models trained in the healthcare domain.
- **Search Through Medical Data:** The bot can search through uploaded medical documents or a database of medical literature to find relevant information. This allows healthcare providers or patients to gain insights from medical documents without going through the entire document themselves.
- **Pre-trained Model Assistance:** By leveraging Hugging Face’s pre-trained models in the medical field (such as BioBERT, ClinicalBERT, or SciBERT), the bot can assist with scientific literature, drug interactions, and treatment plans.

### Tech Stack

* Python 3.11
* Chainlit
* Hugging Face Transformers
* LangChain
* Pinecone
* LiteralAI
* Docker


### Workflow

1. **User Interaction:** Users initiate a conversation with the bot via Chainlit. They can either upload medical documents (PDFs or images) or ask direct questions about medical conditions.
   
2. **Document Splitting & Processing (LangChain):** If a medical report is uploaded, LangChain breaks it down into smaller sections for easier analysis. These smaller sections are then processed for embeddings.
   
3. **Model Inference (Hugging Face Transformers):** The chatbot leverages the pre-trained medical models from Hugging Face to interpret the uploaded data or answer medical queries. The embeddings are generated for the document chunks, and relevant parts of the documents are identified.

4. **Searching for Relevant Information (Pinecone):** If the user asks a question related to the uploaded documents, the embeddings are used to find the most relevant sections in Pinecone’s vector database. This allows the bot to provide context-specific answers based on the user's query.

5. **Response Generation:** The bot generates a response, either by explaining medical terminology, summarizing sections of a medical report, or answering questions related to the user's input.


### Potential Enhancements

- **Fine-tuning for Specific Use Cases:** By further fine-tuning the models on more specific medical datasets (e.g., cardiology, oncology), the chatbot can become more specialized for certain medical fields.
- **Voice Interaction Integration (Whisper + ElevenLabs):** To make the bot more accessible, voice interaction could be integrated using Whisper for speech-to-text and ElevenLabs for text-to-speech, enabling voice queries and responses.
- **Multi-language Support:** For global applications, additional language support could be added using models trained on multilingual medical corpora.
