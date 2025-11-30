import datetime
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.preload_memory_tool import preload_memory_tool as preload_memory
from google.genai import types
#from google.adk.tools import preload_memory
from google.adk.tools.agent_tool import AgentTool

from settings import MODEL_NAME
from memory_callbacks import auto_save_to_memory

from .vocab_agent import build_vocab_agent
from .maths_agent import build_maths_agent
from .validator_agent import build_validator_agent

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

def build_coordinator_agent() -> LlmAgent:

    vocab = AgentTool(agent=build_vocab_agent())
    maths = AgentTool(agent=build_maths_agent())
    validator = AgentTool(agent=build_validator_agent())

    model = Gemini(model=MODEL_NAME, retry_options=retry_config)

    instruction = """
You are the CoordinatorAgent for the Agent11Plus project.

SESSION STATE BEHAVIOUR
-----------------------
When user selects a subject:
    Create session.state["quiz"] = {
        "subject": "vocab" or "maths",
        "current_q": 0,
        "total_q": 5,
        "correct": 0,
        "wrong": [],
        "questions": []
    }

DURING QUIZ:
- Delegate to VocabularyAgent or MathsAgent via tools.
- Each specialist agent updates session.state["quiz"].

AFTER QUIZ:
When quiz is complete (QUIZ_COMPLETE == true):
1. Build a summary:
    { "subject": ..., "correct": ..., "wrong": [...], "date": ... }
2. Save this summary into long-term memory.
3. Provide the learner with:
    - Their score
    - Revision suggestions based on wrong[]
4. End the quiz gracefully.

MEMORY BEHAVIOUR
----------------
Use preload_memory to retrieve:
- Past quiz summaries
- Weak words
- Weak topics
Adapt future quizzes to reinforce weaknesses.

SIMPLE LANGUAGE
---------------
Always speak like a friendly tutor for 9-11 year olds.
"""

    return LlmAgent(
        model=model,
        name="CoordinatorAgent",
        instruction=instruction.strip(),
        tools=[
            preload_memory,
            vocab,
            maths,
            validator,
        ],
        after_agent_callback=auto_save_to_memory,
    )