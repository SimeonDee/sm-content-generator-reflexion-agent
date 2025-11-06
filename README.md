# sm-content-generator-reflexion-agent
An AI agent capable of generating high quality, ground-data-proved social media posts. This multi-agent system follows a [Reflexion Agentic Strategy](https://arxiv.org/abs/2303.11366), providing initial self-reflection responder agent, in collaboration with Revisor agents capable of iterative criticism and revision of generated contents against ground live data for authenticity and quality.

---
`Adedoyin Simeon Adeyemi` | [LinkedIn](https://www.linkedin.com/in/adedoyin-adeyemi-a7827b160/)

---

## Tools Used:

- Langraph (for autonomous multi-agent dev)
- LangChain (for LLM chains)
- Langsmith (for evaluation and monitoring)
- OpenAI GPT4.1-mini (LLM)
- Tavily Search tool (API) (for ground live data internet search and citations)
- pytest (for unittests)
- ruff (for linting)
- black (for code-quality checks)
- mypy (for type-checking)
- make (for generate build commands -- Makefile)
- uv (package management)

## Skills
- Prompt Engineering
- Agentic development
- Tool calling and integration
- LLMs integration
- Reflexion Agent Development
- Unit Testing
- Code quality compliance (linting, type-checking, formating)
- Project/Code Lifecycle CI/CD management (using make -- `Makefile`)


## Setups

A makefile containing development and execution workflow command is available as shown below.
Run the respective command in your terminal/command prompt.

For help on the appropriate command to use, run the command below:

```bash
~ $ make help
```

### 1. Environment Setup:
- `make install`: Creates virtual environment and installs dependencies
- `make dev-setup`: Sets up development environment with all tools

### 2. Development Tasks:
- `make run`: Runs the application
- `make format`: Formats code using black
- `make lint`: Lints code using ruff
- `make type-check`: Runs type checking with mypy
- `make test`: Runs pytest tests

### 3. Maintenance:
- `make clean`: Removes Python bytecode files and caches
- `make check-all`: Runs all checks (format, lint, type-check, test)

### 4. Help:
- `make help`: Shows available commands (default target)

## Steps and Features Implemented:

- [To be updated...]

## Sample Response

**Input Query:**

`Pass`

**Response:**

`Pass`
