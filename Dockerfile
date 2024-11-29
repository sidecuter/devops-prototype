FROM python:3.12-slim
LABEL APP lab3

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt

WORKDIR /opt/app/app

CMD ["python3", "-m", "gunicorn", "-b", "0.0.0.0:3000", "-w", "4", "app:app"]
