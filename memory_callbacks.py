# memory_callbacks.py is used by the Agent to handle memory-related callbacks automatically.

async def auto_save_to_memory(callback_context):
    ctx = getattr(callback_context, "_invocation_context", None)
    if ctx is None:
        return
    
    memory = getattr(ctx, "memory_service", None)
    session = getattr(ctx, "session", None)

    if memory and session:
        await memory.add_session_to_memory(session)


        