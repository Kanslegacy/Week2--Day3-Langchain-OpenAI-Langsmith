"""
Gen AI Architect Program - Assignment 5 (LangChain)

Sends a prompt to an OpenAI chat model via LangChain and prints the response.
LangSmith tracing is enabled purely through environment variables
(LANGCHAIN_TRACING_V2, LANGCHAIN_API_KEY, LANGCHAIN_PROJECT) - LangChain
picks these up automatically, no extra code needed here.

Required environment variables:
    OPENAI_API_KEY        - your OpenAI key
    LANGCHAIN_API_KEY      - your LangSmith key
    LANGCHAIN_TRACING_V2   - set to "true" to enable tracing
    LANGCHAIN_PROJECT      - (optional) LangSmith project name
"""

import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load variables from a local .env file (if present) into the environment.
# This has no effect if the variables are already set some other way.
load_dotenv()


def get_required_env(var_name: str) -> str:
    """Fetch a required environment variable, or exit with a clear error."""
    value = os.environ.get(var_name)
    if not value:
        print(f"Error: required environment variable '{var_name}' is not set.")
        print("Please set it before running this program, e.g.:")
        print(f'  export {var_name}="your-key-here"   # macOS/Linux')
        print(f'  $env:{var_name}="your-key-here"      # Windows PowerShell')
        sys.exit(1)
    return value


def main():
    # Fail fast and clearly if the OpenAI key is missing.
    get_required_env("OPENAI_API_KEY")

    # LangSmith tracing is optional but recommended for this assignment.
    # If LANGCHAIN_TRACING_V2 isn't set to "true", the run just won't be traced -
    # the program still works, it just won't show up on the LangSmith dashboard.
    tracing_enabled = os.environ.get("LANGCHAIN_TRACING_V2", "").lower() == "true"
    if tracing_enabled and not os.environ.get("LANGCHAIN_API_KEY"):
        print("Warning: LANGCHAIN_TRACING_V2 is 'true' but LANGCHAIN_API_KEY is "
              "not set. Tracing will likely fail silently or error out.")

    # ChatOpenAI is LangChain's wrapper around OpenAI's chat models -
    # this is what makes the call go "through LangChain" rather than
    # hitting the OpenAI API directly.
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    prompt = input("Enter your prompt: ").strip()

    if not prompt:
        print("Error: prompt cannot be empty.")
        sys.exit(1)

    print(f"\nInput: {prompt}\n")

    response = llm.invoke([HumanMessage(content=prompt)])

    print(f"Output: {response.content}")

    if tracing_enabled:
        project = os.environ.get("LANGCHAIN_PROJECT", "default")
        print(f"\n(Tracing enabled - check the '{project}' project in LangSmith "
              f"to see this run.)")


if __name__ == "__main__":
    main()
