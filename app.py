import streamlit as st
from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("Homework Helper Crew")

topic = st.text_input("What topic do you need help with?")
difficulty = st.sidebar.selectbox("Difficulty level", ["Beginner", "Intermediate", "Advanced"])

if "runs" not in st.session_state:
    st.session_state.runs = 0

if st.button("Get Help") and topic:
    if st.session_state.runs >= 5:
        st.error("Run limit reached for this session.")
    else:
        st.session_state.runs += 1
        # define agents/tasks here, same as Colab but WITHOUT await
        explainer = Agent(
            role="Concept Explainer",
            goal=f"Explain the given topic clearly at a {difficulty} level",
            backstory="A patient teacher who adapts explanations to the student's level."
        )
        # ... example_writer, question_setter, tasks, context=[...] same as before

        crew = Crew(agents=[...], tasks=[...], process=Process.sequential)
        result = crew.kickoff(inputs={"topic": topic})  # no await here
        st.write(result)
