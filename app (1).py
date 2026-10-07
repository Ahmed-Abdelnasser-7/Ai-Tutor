import os
import streamlit as st
import requests

st.set_page_config(page_title="AI Personal Tutor", page_icon="🎓")
st.title("🎓 AI Personal Tutor")
st.write("Upload a lecture, learn from it, take a quiz, and ask questions about it.")

# Streamlit and FastAPI run in the same Kaggle machine.
# The notebook passes these values automatically, so the user does not enter them.
api_url = os.environ.get("TUTOR_BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")
api_key = os.environ.get("TUTOR_API_KEY", "")
headers = {"X-API-Key": api_key}

if "quiz" not in st.session_state:
    st.session_state.quiz = None
if "result" not in st.session_state:
    st.session_state.result = None

# Check the connection automatically.
try:
    health = requests.get(api_url + "/health", headers=headers, timeout=10)
    if health.ok:
        st.success("Connected to the tutor backend")
    else:
        st.error(f"Backend error: {health.text}")
except Exception as e:
    st.error(f"Could not connect to the backend: {e}")

st.header("1. Upload Book Chapter / Lecture")
file = st.file_uploader("PDF, TXT or Markdown", type=["pdf", "txt", "md"])

if st.button("Index Material"):
    if not file:
        st.error("Choose a file first.")
    else:
        try:
            r = requests.post(
                api_url + "/upload",
                files={"file": (file.name, file.getvalue())},
                headers=headers,
                timeout=180,
            )
            if r.ok:
                data = r.json()
                st.session_state.quiz = None
                st.session_state.result = None
                st.success(f"Indexed {data['filename']} ({data['chunks']} chunks)")
            else:
                st.error(f"Indexing failed: {r.text}")
        except Exception as e:
            st.error(f"Indexing failed: {e}")

st.divider()
st.header("2. Explain the Indexed Lecture")

if st.button("Explain"):
    try:
        r = requests.post(api_url + "/explain", headers=headers, timeout=180)
        if r.ok:
            data = r.json()
            st.subheader(data["topic"])
            st.write(data["explanation"])
            st.write("**Example:**")
            st.write(data["example"])
        else:
            st.error(r.text)
    except Exception as e:
        st.error(f"Explain failed: {e}")

st.divider()
st.header("3. Generate Questions")
number = st.number_input("Number of questions", 1, 10, 5)

if st.button("Generate Quiz"):
    try:
        r = requests.post(
            api_url + "/quiz",
            json={"number": int(number)},
            headers=headers,
            timeout=180,
        )
        if r.ok:
            st.session_state.quiz = r.json()
            st.session_state.result = None
        else:
            st.error(r.text)
    except Exception as e:
        st.error(f"Quiz failed: {e}")

if st.session_state.quiz:
    answers = {}
    for q in st.session_state.quiz["questions"]:
        st.write(f"**{q['id']}. {q['question']}**")
        answers[str(q["id"])] = st.radio(
            "Answer:",
            q["options"],
            key=f"q_{q['id']}",
        )

    if st.button("Submit Answers"):
        try:
            r = requests.post(
                api_url + "/evaluate",
                json={
                    "quiz_id": st.session_state.quiz["quiz_id"],
                    "answers": answers,
                },
                headers=headers,
                timeout=180,
            )
            if r.ok:
                st.session_state.result = r.json()
            else:
                st.error(r.text)
        except Exception as e:
            st.error(f"Evaluation failed: {e}")

if st.session_state.result:
    result = st.session_state.result
    st.divider()
    st.header("4. Score & Feedback")
    st.metric("Student Score", f"{result['score']}/{result['max_score']}")
    st.write(f"**{result['percent']}%**")
    st.write(result["overall_feedback"])

    for item in result["results"]:
        st.write(f"**Question {item['id']}**")
        st.write(f"Your answer: {item['student_answer']}")
        st.write(f"Correct answer: {item['correct_answer']}")
        st.write(f"Feedback: {item['feedback']}")

st.divider()
st.header("5. Ask the Tutor")
question = st.text_area("Ask about the uploaded material")

if st.button("Ask"):
    try:
        r = requests.post(
            api_url + "/ask",
            json={"question": question},
            headers=headers,
            timeout=180,
        )
        if r.ok:
            st.write(r.json()["answer"])
        else:
            st.error(r.text)
    except Exception as e:
        st.error(f"Question failed: {e}")

st.divider()
st.header("6. Student Memory")

try:
    r = requests.get(api_url + "/memory", headers=headers, timeout=30)
    if r.ok:
        memory = r.json()
        st.write(f"Quiz attempts: {memory['attempts']}")
        st.write(f"Last score: {memory['last_score']}%" if memory['last_score'] is not None else "Last score: None")
        if memory["scores"]:
            st.write("Previous scores:", memory["scores"])
except Exception as e:
    st.error(f"Memory error: {e}")
