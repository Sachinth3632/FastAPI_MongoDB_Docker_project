FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir pymongo fastapi uvicorn && \
    pip uninstall -y bson || true

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
