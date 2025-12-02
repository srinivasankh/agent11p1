# agents/validator_agent.py

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from settings import MODEL_NAME


def build_validator_agent() -> LlmAgent:
    model = Gemini(model=MODEL_NAME)

    instruction = """
You validate MCQs created by the VocabularyAgent or MathsAgent.

You check:
- Is the question age appropriate?
- Is there ONE correct answer?
- Is the explanation clean and simple?
- If something is wrong, produce a corrected version.

Return:
    verdict: OK or NEEDS_FIX
    corrected_question: (if needed)
"""

    return LlmAgent(
        model=model,
        name="ValidatorAgent",
        instruction=instruction.strip(),
    )