import logging
import os
from dotenv import load_dotenv

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, WorkerType, cli
from livekit.plugins import openai, tavus, deepgram, rime

logger = logging.getLogger("tavus-avatar-example")
logger.setLevel(logging.INFO)

load_dotenv()


async def entrypoint(ctx: JobContext):
    # ✅ Step 0: Connect to room context
    await ctx.connect()

    # using only OpenAI LLM for tts, stt
    session = AgentSession(
        llm=openai.realtime.RealtimeModel(voice="alloy"),
    )


    # session = AgentSession(
    #     llm=openai.LLM(model="gpt-4o-mini"),
    #     stt=deepgram.STT(model="nova-3"),
    #     tts=rime.TTS(
    #         model="mistv2",
    #         speaker="grove",
    #         speed_alpha=1.1,
    #         reduce_latency=True,
    #     ),
    # )

    persona_id = os.getenv("TAVUS_PERSONA_ID")
    replica_id = os.getenv("TAVUS_REPLICA_ID")
    tavus_avatar = tavus.AvatarSession(
        persona_id=persona_id,
        replica_id=replica_id
    )

    # ✅ Step 1: Start agent session
    await session.start(
        agent=Agent(instructions="Your name is Tanmay."),
        room=ctx.room,
    )

    # ✅ Step 2: Start Tavus avatar session
    await tavus_avatar.start(session, room=ctx.room)

    # ✅ Step 3: Say something
    await session.generate_reply(instructions="Say hello to the user")

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(entrypoint_fnc=entrypoint, worker_type=WorkerType.ROOM)
    )
