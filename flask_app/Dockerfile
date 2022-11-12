FROM python:3.10-slim-buster
WORKDIR .
COPY requirements.txt .
RUN pip install --no-cache-dir -U -r  requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]