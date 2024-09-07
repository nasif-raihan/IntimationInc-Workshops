FROM python:3.12-slim AS requirements

WORKDIR /app
RUN pip3 install -U pip poetry
COPY pyproject.toml ./
RUN poetry export --only main --format requirements.txt --output requirements.txt

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
RUN pip3 install -U pip
COPY --from=requirements /app/requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "main.py"]