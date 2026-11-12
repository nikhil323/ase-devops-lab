# ase-devops-lab

Weekly DevOps practice for COMP-8117 (Advanced Software Engineering Topics, Fall 2026).

The goal is to close my DevOps gap (CI/CD, Docker, AWS) one small step per week.

## Run locally

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Run the API

```
uvicorn app.main:app --port 8000
```

Then open http://localhost:8000/docs

In Docker:

```
docker build -t ase-devops-lab .
docker run --rm -p 8000:8000 ase-devops-lab uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Licenses

This project: MIT (see LICENSE).

fastapi -> 0.162.2 -> MIT
httpx -> 0.28.1 -> BSD-3-Clause
uvicorn -> 0.54.0 -> BSD-3-Clause
pytest -> 9.1.1 -> MIT