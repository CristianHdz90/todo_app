FROM python:3.9.7

LABEL maintainer="CristianHdz90, hernandezcamilo063@gmail.com"

WORKDIR /todo_app

COPY [".", "."]

RUN pip install -r /todo_app/src/requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="/todo_app/config/KeyFile.json"

CMD ["gunicorn", "--chdir", "./src", "--bind", "0.0.0.0:$PORT", "main:app"]