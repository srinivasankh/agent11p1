APP_NAME = "agent_11plus_app"

# Model selection for Agent 11Plus
# For interactive quiz generation, fast models are preferred over powerful but slow models

MODEL_NAME = "gemini-2.0-flash-exp"  # RECOMMENDED: Fast, reliable, great for interactive quizzes
#MODEL_NAME = "gemini-1.5-flash-latest"  # Alternative: Proven stable, very fast
#MODEL_NAME = "gemini-1.5-flash-8b"  # Budget: Fastest, cheapest, still good for simple quizzes
#MODEL_NAME = "gemini-1.5-pro-latest"  # More powerful but slower (unnecessary for this use case)
#MODEL_NAME = "gemini-2.0-pro-preview"  # Latest SOTA: Powerful but SLOW (overkill for MCQ generation)

# This is only for local demo
# For a real app we could derive user_id from auth
DEFAULT_USER_ID = "local-demo-user"