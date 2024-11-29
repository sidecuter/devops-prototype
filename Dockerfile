FROM python:3.12-slim
LABEL APP lab3

WORKDIR /opt/app

RUN python -m venv /opt/app/venv

ENV PATH="/opt/app/venv/bin:$PATH"

COPY . .

WORKDIR /opt/app/app

CMD ["/opt/app/venv/bin/gunicorn" "-b" "0.0.0.0:3000" "-w" "4" "app:app"]
