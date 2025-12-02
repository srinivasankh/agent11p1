import asyncio
import logging
from dotenv import load_dotenv

# Suppress spurious warnings from google.adk and google.genai
# 1. "App name mismatch" - incorrectly checks base class location instead of where agents are defined
# 2. "non-text parts in the response" - informational warning about function calls in responses
logging.getLogger('google_adk.google.adk.runners').setLevel(logging.ERROR)
logging.getLogger('google_adk').setLevel(logging.ERROR)
logging.getLogger('google_genai.types').setLevel(logging.ERROR)

from google.adk.runners import Runner
from google.adk.apps import App
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types

from settings import APP_NAME, DEFAULT_USER_ID
from agent_11plus_app.coordinator_agent import build_coordinator_agent


def build_runner():
    load_dotenv()

    session_service = InMemorySessionService()
    memory_service = InMemoryMemoryService()
    coordinator = build_coordinator_agent()

    app = App(
        name=APP_NAME,
        root_agent=coordinator,
    )

    runner = Runner(
        app=app,
        session_service=session_service,
        memory_service=memory_service,
    )

    return runner

async def chat_loop():
    runner = build_runner()
    session_id = "demo-session"


    await runner.session_service.create_session(
        app_name=APP_NAME,
        user_id=DEFAULT_USER_ID,
        session_id=session_id
    )

    print("👋 Welcome to Agent 11Plus!")
    print("Ask: 'I want to revise vocabulary' or 'I want to revise maths'")
    print("Type 'exit' to quit.\n")

    while True:
        msg = input("You: ").strip()
        if msg.lower() == "exit":
            break

        content = types.Content(
            role="user",
            parts=[types.Part(text=msg)]
        )

        async for event in runner.run_async(
            user_id=DEFAULT_USER_ID,
            session_id=session_id,
            new_message=content,
        ):
            if event.is_final_response() and event.content and event.content.parts:
                reply = event.content.parts[0].text
                if reply:
                    print(f"\nAgent: {reply}\n")


if __name__ == "__main__":
    asyncio.run(chat_loop())

