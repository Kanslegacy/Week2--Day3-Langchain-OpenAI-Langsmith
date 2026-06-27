# LangChain + OpenAI + LangSmith — Assignment 5

A minimal Python app that sends a prompt to an OpenAI chat model **through LangChain**
and prints the response. Every run is traced in **LangSmith**.

## Files in this project

```
langchain-app/
├── main.py            # the app (already provided)
├── requirements.txt   # dependencies
├── .env.example       # template for your keys (safe to commit)
├── .env               # your real keys (NEVER commit this)
└── .gitignore         # tells git to ignore .env and venv/
```

## Step 1 — Create the project folder

```bash
mkdir langchain-app
cd langchain-app
```

Put `main.py`, `requirements.txt`, `.env.example`, and `.gitignore` (all provided below)
into this folder. Open the folder in VS Code: `code .`

## Step 2 — Create a virtual environment

```bash
python -m venv venv
```

(Use `python3` instead of `python` if that's what your system uses.)

## Step 3 — Activate it

```bash
# macOS / Linux
source venv/bin/activate

# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows Command Prompt
venv\Scripts\activate.bat
```

You'll see `(venv)` appear at the start of your terminal prompt when it's active.

> **VS Code tip:** open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) →
> "Python: Select Interpreter" → pick the one inside `venv/` so VS Code uses
> the same environment as your terminal.

## Step 4 — Install dependencies

```bash
pip install -r requirements.txt
```

## Step 5 — Set up your API keys

1. Copy the template into a real `.env` file:

   ```bash
   # macOS / Linux
   cp .env.example .env

   # Windows
   copy .env.example .env
   ```

2. Open `.env` in VS Code and fill in your real keys:
   - **OpenAI key**: from [platform.openai.com](https://platform.openai.com)
   - **LangSmith key**: from [smith.langchain.com](https://smith.langchain.com)

3. `main.py` loads `.env` automatically at startup (via `python-dotenv`), so
   you don't need to export the variables manually in your terminal. Just
   make sure `.env` sits in the same folder as `main.py`.

## Step 6 — Run it

```bash
python main.py
```

You should see something like:

```
Enter your prompt: Tell me a fun fact about Tamil Nadu.

Input: Tell me a fun fact about Tamil Nadu.

Output: <the model's response>

(Tracing enabled - check the 'langchain-assignment' project in LangSmith to see this run.)
```

Then open [smith.langchain.com](https://smith.langchain.com), go to your project
(`langchain-assignment` by default), and confirm the run appears with input,
output, and timing.

## Step 7 — Deactivate when done

```bash
deactivate
```

## Before pushing to GitHub

- Double check `.env` is listed in `.gitignore` (it already is, below).
- Run `git status` and confirm `.env` does **not** show up as a file to be committed.
- Only `.env.example` (with placeholder text, no real keys) should be tracked.

```bash
git init
git add .
git status   # sanity check: .env should NOT appear here
git commit -m "Assignment 5: LangChain + OpenAI + LangSmith"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Troubleshooting

| Problem | Likely cause |
|---|---|
| `Error: required environment variable 'OPENAI_API_KEY' is not set` | `.env` missing, misnamed, or not in the same folder as `main.py` |
| No run shows up in LangSmith | `LANGCHAIN_TRACING_V2` isn't exactly `"true"`, or `LANGCHAIN_API_KEY` is wrong |
| `ModuleNotFoundError` | venv not activated, or `pip install -r requirements.txt` wasn't run inside it |
| Authentication error from OpenAI | Key copied with extra spaces/quotes, or billing not set up on your OpenAI account |
