FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install streamlit

EXPOSE 8501

ENV PYTHONPATH="/app:${PYTHONPATH}"

CMD ["streamlit", "run", "app/ui/main.py", "--server.port=8501", "--server.address=0.0.0.0"]