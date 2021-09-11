FROM python:3.9.7

LABEL maintainer="CristianHdz90, hernandezcamilo063@gmail.com"

RUN mkdir -p todo_app/src

WORKDIR /todo_app

COPY ["src/requirements.txt", "./src"]

RUN pip install -r src/requirements.txt

COPY [".", "."]

ENV FLASK_APP="./src/main.py"

ENV FLASK_ENV="development"

#This secret key is only for development, don't use it in production.
ENV SECRET_KEY_FLASK="b8RFf?3=_Mfcfu6=H=RXeX*BX_jM-M*V&GD5%nZfenwL!=*!"

ENV GOOGLE_APPLICATION_CREDENTIALS="/todo_app/config/KeyFile.json"

CMD ["tail", "-f", "/dev/null"]