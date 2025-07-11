# AI-Avatar-Agent-with-LiveKit-Tavus

This project demonstrates how to build an AI-powered avatar agent using [LiveKit](https://livekit.io/) for real-time audio/video, [Tavus](https://tavus.io/) for avatar generation, and [OpenAI](https://openai.com/) for conversational intelligence.

## Features

- Real-time agent joins a LiveKit room and interacts with users
- AI-generated speech and responses using OpenAI
- Avatar video generation and control via Tavus
- Speech-to-text and TTS support (Deepgram, Rime)

## Folder Structure

```
.
├── agent_worker.py      # Main agent and avatar logic
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
├── temp.txt             # Temporary notes/links
└── venv/                # Python virtual environment (not committed)
```

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/ChitrakshSuri/AI-Avatar-Agent-with-LiveKit-Tavus-Working.git
   cd AI-Avatar-Agent-with-LiveKit-Tavus
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # source venv/bin/activate   # On macOS/Linux
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   # Or, if using extras:
   pip install "livekit-agents[tavus]~=1.0"
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root with the following content (replace with your actual keys):

   ```
   # LiveKit config
   LIVEKIT_URL=your_livekit_url
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret

   # OpenAI config
   OPENAI_API_KEY=your_openai_api_key

   # Speech-to-Text and TTS
   DEEPGRAM_API_KEY=your_deepgram_api_key
   RIME_API_KEY=your_rime_api_key

   # Tavus Avatar config
   TAVUS_API_KEY=your_tavus_api_key
   TAVUS_REPLICA_ID=your_tavus_replica_id
   TAVUS_PERSONA_ID=your_tavus_persona_id
   ```

5. **Download required files**
   ```sh
   python agent_worker.py download-files
   ```

6. **Run the agent**
   ```sh
   python agent_worker.py dev
   ```

## Usage

- The agent will join the specified LiveKit room and interact with users using AI-generated responses and avatar video.
- You can monitor and interact with the agent using the [LiveKit Agents Playground](https://agents-playground.livekit.io/).

## References

- [LiveKit Agents Example](https://github.com/livekit/agents/blob/main/examples/avatar_agents/tavus/agent_worker.py)
- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [Tavus API Documentation](https://docs.tavus.io/)
- [YouTube Demo](https://www.youtube.com/watch?v=ftFjm6qz-8M)

## License

MIT License

---

**Note:**  
Do not commit your `.env` or `venv/` folders. See `.gitignore` for details.
