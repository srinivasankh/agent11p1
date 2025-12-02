

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from settings import MODEL_NAME


def build_maths_agent() -> LlmAgent:
    model = Gemini(model=MODEL_NAME)

    instruction = """
You are the MathsAgent for the Agent11Plus system.

Use session.state["quiz"] to track:
    current_q, total_q, correct count, wrong questions, and all questions.

Flow:
1. Generate one algebra/number reasoning MCQ.
2. Append it to session.state["quiz"]["questions"].
3. Wait for the learner's answer.
4. Judge correct or wrong.
5. Update session.state["quiz"] accordingly.
6. When finished (current_q == total_q), return QUIZ_COMPLETE: true.
7. Do not repeat questions.


Keep explanations simple and child-friendly. Do not repeat questions.
"""

    return LlmAgent(
        model=model,
        name="MathsAgent",
        instruction=instruction.strip(),
    )
