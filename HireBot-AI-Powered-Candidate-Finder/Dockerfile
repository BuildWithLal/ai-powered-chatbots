FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN python -m venv .venv

SHELL ["/bin/bash", "-c"]
RUN source .venv/bin/activate

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "chainlit", "run", "app.py", "--watch", "--headless"]
