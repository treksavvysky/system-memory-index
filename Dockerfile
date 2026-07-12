FROM python:3.11-slim

WORKDIR /app

COPY . /app/

ENTRYPOINT ["python3", "smi_generator.py"]
