# LLM Learning Plan (Data + AI)

Goal: combine SQL/PL/SQL strength with Python and LLMs. 30-45 minutes a day, one small thing saved every day.

Use only a personal laptop and personal accounts. No Infosys client data, code, or accounts.

---

## Part 1: Day 1 setup checklist

- [x] Python 3.12 installed (`python --version` works)
- [x] pip works (`pip --version`)
- [x] Project folder `llm-learning` created
- [x] Virtual environment created and activated (`(venv)` shows in prompt)
- [x] VS Code installed, Python extension added
- [x] `hello.py` runs

### Still to do today

1. Keep every file directly inside `llm-learning`. Never put files inside `venv`.
2. Save this file as `PLAN.md` in `llm-learning`.
3. Create `progress.md` in the same folder (template at the bottom).
4. Create `.gitignore` containing this one line:
   ```
   venv/
   ```
5. Save the work in Git (terminal, inside `llm-learning`):
   ```
   git init
   git add .
   git commit -m "Day 1: setup and first script"
   ```
   If Git is not recognized, install it from git-scm.com and open a new terminal.
6. Create an empty repo named `llm-learning` on github.com (personal account), then run the two commands GitHub shows under "push an existing repository".

### Commands to remember

| Task | Command |
|---|---|
| Activate venv | `.\venv\Scripts\Activate.ps1` |
| Run a script | `python hello.py` (always type `python` first) |
| Install a library | `pip install pandas` (only while `(venv)` is active) |
| Save work | `git add .` then `git commit -m "message"` then `git push` |

---

## Part 2: 14-week plan

### Phase 1: Python basics (weeks 1-3)
- **Week 1:** variables, loops, functions, lists and dicts. Small scripts daily.
- **Week 2:** files, error handling, modules. Read and write CSV/JSON.
- **Week 3:** pandas. Redo your usual SQL tasks (filter, group by, join).

### Phase 2: Data + databases (weeks 4-6)
- **Week 4:** connect Python to Oracle with `oracledb`. Run queries into pandas.
- **Week 5:** script that pulls data from Oracle, cleans it, exports a report.
- **Week 6:** Git/GitHub for all projects. **Checkpoint:** read 20-30 job postings and compare to your skills.

### Phase 3: LLM fundamentals (weeks 7-10)
- **Week 7:** call the Anthropic API from Python. Prompts, system prompts, parameters.
- **Week 8:** structured outputs (JSON), tool use / function calling.
- **Week 9:** embeddings and basic RAG.
- **Week 10:** start Project 1 (Text-to-SQL assistant).

### Phase 4: Portfolio and career (weeks 11-14)
- **Weeks 11-12:** polish Project 1 (README, demo video, Streamlit UI).
- **Week 13:** Project 2 (RAG document Q&A) or a smaller project.
- **Week 14:** update resume and LinkedIn, start applying or pitching freelance clients.

Optional weekend add-on after Phase 2: build one Custom GPT and one Copilot Studio agent.

---

## Part 3: Week 1 daily tasks

| Day | Task |
|---|---|
| 1 | Setup and `hello.py` (done) |
| 2 | List of 5 numbers; function returning the sum and the largest, without `sum()` or `max()` |
| 3 | Dictionary of 5 employees and salaries; print those above the average |
| 4 | Loop with `if/elif/else`: grade calculator |
| 5 | Function that counts word frequency in a sentence |
| 6 | Combine days 2-5 into one small program with a menu |
| 7 | Review, clean up code, commit to GitHub, update `progress.md` |

---

## Part 4: Two portfolio projects

### Project 1: Chat with your database (Text-to-SQL), about 4 weeks
1. **Week 1:** sample Oracle schema (HR/SH). Script sends schema + question to Claude and gets SQL back.
2. **Week 2:** safety. Allow only `SELECT`, validate SQL, add row limits, use a read-only DB user.
3. **Week 3:** run the query, return results, have the LLM explain them, retry when SQL errors.
4. **Week 4:** Streamlit UI, show generated SQL beside the answer, test 30+ questions, README with an accuracy table.

### Project 2: Document Q&A with RAG, about 4-5 weeks
1. **Week 1:** load and clean documents, split into chunks.
2. **Week 2:** embeddings and a vector store (Chroma or FAISS).
3. **Week 3:** retrieve top chunks, answer only from context, include citations.
4. **Week 4:** evaluation set of 20-30 questions; tune chunk size, top-k, prompts.
5. **Week 5:** Streamlit UI, deploy, README with architecture diagram and results.

Tip: use PL/SQL code and documentation as the document set to make it unique.

---

## Part 5: Ask your AI assistant for guidance

With this folder open in VS Code, ask the assistant:

> Read PLAN.md and progress.md, then tell me what to do today and review my latest code.

Write first versions yourself. Use AI to explain, review, and debug.

---

## progress.md template

```
# Progress log

## 2026-10-04
- Done: Python 3.12, venv, VS Code set up; hello.py runs
- Confused about: (write here)
- Next: Week 1 Day 2 task
```
