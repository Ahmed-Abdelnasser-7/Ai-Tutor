# 🎓 AI Personal Tutor — RAG + Memory + Output Parser

> 🤖 An AI-powered personal tutor that helps students learn from their own uploaded books and lecture notes using Retrieval-Augmented Generation (RAG), student memory, and structured output parsing.

---

## 👤 Participant

| Field            | Value                                       |
| ---------------- | ------------------------------------------- |
| Full Name        | Ahmed Abdelnasser Elshamandy                |
| Project Name     | AI Personal Tutor                           |
| GitHub Username  | Ahmed-Abdelnasser-7                         |
| Internship Batch | August–October 2026                         |
| Training Program | Large Language Models (LLMs) Program        |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en) |

---

# 📖 Project Overview

The **AI Personal Tutor** is an AI-based learning assistant designed to help students study from their own educational materials.

The student can upload a **book, chapter, or lecture notes**, and the system processes the material, divides it into smaller chunks, creates embeddings, and stores them in a **FAISS vector database**.

When the student asks a question, the system retrieves the most relevant parts of the uploaded lecture and provides an answer based on the available study material.

The system also includes simple **student memory** to keep track of quiz attempts, previous scores, and feedback.

The project uses **Mistral Nemo** as the language model and provides a simple web interface through **Streamlit**, with **FastAPI** handling the backend services.

---

# ✨ Features

* 📚 Upload lecture notes, books, or chapters in PDF, TXT, or Markdown format.
* ✂️ Split educational material into smaller text chunks.
* 🔎 Retrieve relevant information using RAG.
* 🧠 Generate embeddings using Sentence Transformers.
* 🗄️ Store and search embeddings using FAISS.
* 🤖 Use Mistral Nemo to generate tutor responses.
* 💬 Ask questions about the indexed lecture.
* 📝 Generate quizzes based only on the uploaded lecture.
* ✅ Evaluate student answers.
* 📊 Calculate student scores.
* 💡 Provide feedback based on quiz performance.
* 🧠 Keep simple student memory containing quiz attempts and previous scores.
* 📦 Use an output parser to convert AI responses into structured data.
* ⚡ FastAPI backend for the AI services.
* 🖥️ Streamlit frontend for interacting with the tutor.
* 🌐 Use ngrok to access the Streamlit application from a browser.

---

# 🛠️ Technologies Used

### Artificial Intelligence

* **Mistral Nemo Instruct**
* **Hugging Face Transformers**
* **Sentence Transformers**
* **Retrieval-Augmented Generation (RAG)**

### Backend

* **Python**
* **FastAPI**
* **Pydantic**

### Vector Search

* **FAISS**
* **Sentence Transformer Embeddings**

### Frontend

* **Streamlit**

### Deployment / Environment

* **Kaggle Notebook**
* **ngrok**
* **Kaggle Secrets**

### File Processing

* **PyPDF**

---

# 🏗️ System Architecture

```text
              📚 Book / Lecture Notes
                       │
                       ▼
                📄 File Upload
                       │
                       ▼
                Text Extraction
                       │
                       ▼
                  Text Splitting
                       │
                       ▼
            Sentence Transformer
                 Embeddings
                       │
                       ▼
                    FAISS
               Vector Database
                       │
                       ▼
              🔎 Relevant Chunks
                       │
                       ▼
                Mistral Nemo
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
          Explain    Generate   Evaluate
          Lecture     Quiz      Answers
             │         │         │
             └─────────┼─────────┘
                       ▼
                Output Parser
                       │
                       ▼
              Structured Output
                       │
                       ▼
              Student Feedback
                       │
                       ▼
                Student Memory
```

---

# ⚙️ Installation

The project is designed to run in a **Kaggle Notebook** with GPU support.

### 1. Open the Kaggle Notebook

Upload or open the provided AI Personal Tutor notebook in Kaggle.

### 2. Enable GPU

From Kaggle:

```text
Settings → Accelerator → GPU
```

### 3. Configure Kaggle Secrets

Add the required secrets to the Kaggle notebook:

```text
HF_TOKEN
NGROK_AUTH_TOKEN
TUTOR_API_KEY
```

### 4. Install Dependencies

The notebook installs the required Python packages automatically, including:

```text
transformers
accelerate
bitsandbytes
sentence-transformers
faiss-cpu
pypdf
fastapi
uvicorn
pyngrok
streamlit
pydantic
```

### 5. Run the Notebook

Run the notebook cells from top to bottom.

The notebook will:

1. Load Mistral Nemo.
2. Load the embedding model.
3. Start the FastAPI backend.
4. Start the Streamlit application.
5. Create an ngrok tunnel.
6. Provide a public URL for the Streamlit interface.

---

# 🚀 Usage

After starting the notebook, open the generated **Streamlit URL**.

### Step 1 — Upload Material

Upload one of the supported formats:

```text
PDF
TXT
MD
```

For example:

```text
Data Structures Lecture 1.pdf
```

### Step 2 — Index the Lecture

The system:

```text
Lecture
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
FAISS
```

After indexing, the lecture becomes available to the AI tutor.

### Step 3 — Ask the Tutor

Ask questions related to the uploaded lecture.

For example:

```text
What is a linked list?
```

The system retrieves relevant lecture content and sends it to Mistral Nemo.

The answer is generated using the indexed material.

### Step 4 — Generate a Quiz

The tutor can generate questions based on the indexed lecture.

The questions are generated from the retrieved study material rather than unrelated external information.

### Step 5 — Submit Answers

The student submits their answers.

The system evaluates the answers and calculates:

```text
Score
Percentage
Correct Answers
Feedback
```

### Step 6 — Student Memory

The system keeps simple information about the student's learning progress, including:

```text
Quiz Attempts
Previous Scores
Last Score
```

This information can be used to provide more relevant feedback.

---

# 📸 Demo

Add screenshots or a demonstration video here.

Recommended screenshots:

### 1. Upload Lecture

```text
![Upload Lecture](screenshots/upload.png)
```

### 2. Indexed Lecture

```text
![Indexed Lecture](screenshots/indexed.png)
```

### 3. Ask the Tutor

```text
![Ask Tutor](screenshots/ask-tutor.png)
```

### 4. Quiz

```text
![Quiz](screenshots/quiz.png)
```

### 5. Student Feedback

```text
![Feedback](screenshots/feedback.png)
```

### Demo Video

Add your project demonstration video here.

---

# 📈 Results

The project provides a complete learning workflow where a student can:

```text
Upload Study Material
        ↓
Index Lecture
        ↓
Ask Questions
        ↓
Generate Quiz
        ↓
Submit Answers
        ↓
Receive Score
        ↓
Receive Feedback
        ↓
Track Previous Attempts
```

The project demonstrates the practical use of:

* Retrieval-Augmented Generation.
* Vector similarity search.
* Embeddings.
* Large Language Models.
* Structured output parsing.
* Simple memory.
* FastAPI backend development.
* Streamlit frontend development.

---

# 🔮 Future Improvements

* 👤 Support multiple students with separate memory.
* 💾 Add persistent student memory.
* 📚 Support multiple indexed books and lectures.
* 📑 Allow students to select a specific chapter.
* 📊 Add detailed learning-progress dashboards.
* 🎯 Generate quizzes based on the student's weak areas.
* 🗣️ Add voice-based interaction.
* 🌍 Add multilingual tutoring.
* 🔐 Add proper user authentication.
* ☁️ Deploy the backend and frontend to a permanent cloud service.

---

# 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
