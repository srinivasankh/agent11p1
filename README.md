## Agent 11Plus App

Agent 11Plus is a conversational study companion tailored to U.K. 11+ exam preparation. It uses Google's Agent Development Kit to coordinate a set of domain-focused tools (maths, vocabulary, study coaching) and surfaces dialog through a simple terminal chat loop. Sessions run entirely locally with in-memory stores for session tracking and recall, so you can iterate quickly without additional infrastructure.

### Features
- Gemini-backed coordinator agent that routes user requests to specialist tools.
- Interactive CLI chat loop for quick testing and demo conversations.
- In-memory session and memory services so nothing is persisted beyond a run.
- `.env`-driven configuration to keep API keys out of source control.

### Prerequisites
- Python 3.11+ (the project was bootstrapped with `uv`, but any modern interpreter works).
- A Google Generative AI API key with access to the referenced Gemini model.
- `uv` or `pip`/`venv` for dependency management.

### Local Setup
1. **Clone the repo**
   ```bash
   git clone https://github.com/srinivasankh/agent11p1.git
   cd agent11p1
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   uv sync  # uses pyproject.toml + uv.lock for reproducible installs
   ```
   If you prefer plain pip, install from the project root so it reads `pyproject.toml`:
   ```bash
   pip install .
   ```
4. **Configure environment variables**
   - Copy `.env.example` to `.env`.
   - Add `GOOGLE_API_KEY` (or whichever variable your setup expects) plus any other config.
   - Never commit the real `.env`; it is ignored through `.gitignore`.

### Running the CLI Demo
```bash
python main.py
```
You will see a welcome prompt. Try instructions such as `I want to revise vocabulary` or `I want to revise maths`. Type `exit` to stop.

### Running Locally with the ADK CLI
If you prefer the ADK developer workflow you can let the toolkit scaffold a local web runner for the app.

1. Ensure `google-adk` is installed (e.g., `pip install google-adk`) and that your `.env` is populated with the required keys.
2. From the project root run:
   ```bash
   adk web
   ```
3. The ADK CLI will launch the default web experience in your browser against your local build, so you can iterate on tools and coordinator logic with the familiar ADK dashboards.

### Testing & Troubleshooting
- If the CLI cannot find your API key, confirm the `.env` file exists and matches the names expected by `load_dotenv()` in `main.py`.
- Use `uv pip list` (or `pip list`) to verify that `google-adk` and `google-genai` installed successfully.
- For verbose debugging, instrument `build_runner()` in `main.py` with temporary prints/logging and rerun the CLI.

### Acknowledgements
Huge thanks to Kaggle's [5-Day AI Agent course](https://www.kaggle.com/learn-guide/5-day-agents) for the structure and inspiration that guided this project, and to the [Kaggle Agents Intensive Capstone Project](https://www.kaggle.com/competitions/agents-intensive-capstone-project) that motivated building and polishing this demo!
