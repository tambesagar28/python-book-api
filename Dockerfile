FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY books_api.py .
CMD ["python", "books_api.py"]
