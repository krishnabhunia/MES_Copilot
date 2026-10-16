# LangChain and LLM agent proof-of-concepts

## What the source implements
A group of AI experiments using LangChain prompt templates, Groq-backed chat models and tool-calling agents; these are independent proofs of concept.

**Technology:** Python, LangChain, langchain-groq, notebooks, externally hosted LLM models.

## Code/data inventory
| File | Responsibility |
|---|---|
| `code/py_files/poc1.py` | PromptTemplate experiment |
| `code/py_files/poc2.py` | ChatGroq message invocation demo |
| `code/py_files/poc3.py` | Tool-calling mathematics assistant prototype |
| `code/py_files/poc4.py` | Tool-calling agent experiment |
| `code/nb_files/` | Experimental notebooks |

## Architecture
~~~mermaid
flowchart LR
 User[Notebook / CLI user] --> Entry[PoC scripts and notebooks]
 Entry --> Logic[LangChain agents and tools]
 Logic --> External[Remote Groq model API]
~~~

## Request / processing sequence
~~~mermaid
sequenceDiagram
 participant User
 participant Program
 participant Dependency
 User->>Program: Run selected workflow
 Program->>Dependency: Load data or call library/service
 Dependency-->>Program: Values / response / error
 Program-->>User: Display result
~~~

## Installation and setup
1. Create a Python virtual environment (Python 3.12 is a reasonable baseline, but original code has no pinned Python version).
2. Install compatible versions of langchain, langchain-core and langchain-groq after reviewing current package APIs; no lockfile is provided.
3. Configure the required Groq API credentials through environment variables or a local secret store; never commit them.
4. Run individual files from code/py_files only after confirming the named remote models still exist and the dependency versions match.

~~~mermaid
flowchart TD
 Clone[Clone or open repository] --> Install[Select Python environment]
 Install --> Dependencies[Review and install required packages]
 Dependencies --> Data[Provide local input / credentials if required]
 Data --> Execute[Run selected example]
 Execute --> Check{Expected outcome?}
 Check -->|Yes| Test[Review tests and output]
 Check -->|No| Fix[Diagnose versions and input]
 Fix --> Dependencies
~~~

## Program behavior
poc1 creates a prompt; other scripts invoke remote Groq chat models and agents, with sample arithmetic tools. A remote API call can incur costs and requires valid credentials.

## Validation and reproducibility
- GitHub Actions validates the README's guide link, Markdown fences and three Mermaid diagrams.
- CI compiles Python scripts and validates notebook JSON, without invoking costly external LLM APIs.
- End-to-end usage must be checked using the setup steps above; do not imply remote APIs or datasets are available by default.

## Limitations and further work
- No dependency lockfile or safe offline integration fixtures.
- Legacy model identifiers and LangChain APIs may have changed; runtime compatibility is not verified by syntax checks.
- Some sample tools are placeholders or may produce incomplete responses; do not present them as finished production agents.
- No actual geographic outputs or performance statistics are committed, so neither fabricated maps nor invented performance charts belong in this guide.
- Application logic and dependencies are left unchanged by this documentation-only PR.
