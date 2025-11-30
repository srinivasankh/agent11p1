# agents/vocab_agent.py

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

from settings import MODEL_NAME


def build_vocab_agent() -> LlmAgent:
    model = Gemini(model=MODEL_NAME)

    instruction = """
You are the VocabularyAgent for the Agent11Plus system.

Inside each session:
- The coordinator will initialise session.state["quiz"] with:
    { "subject": "vocab",
      "current_q": 0,
      "total_q": 5,
      "correct": 0,
      "wrong": [],
      "questions": [] }

Your responsibilities:
1. Generate one vocabulary MCQ at a time.
2. Append the generated question to session.state["quiz"]["questions"].
3. Wait for the learner’s answer.
4. Check their answer, update:
      correct++, or append wrong word to wrong[].
5. When the session reaches total_q, return QUIZ_COMPLETE: true.
6. Use very simple language for 9–11 year olds.
"""

    return LlmAgent(
        model=model,
        name="VocabularyAgent",
        instruction=instruction.strip(),
    )