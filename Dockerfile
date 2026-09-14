FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r req.txt

COPY . .

EXPOSE 5003

CMD ["python", "app.py"]
