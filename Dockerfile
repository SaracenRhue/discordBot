FROM python:3.10-slim

WORKDIR /home/app

COPY . .

RUN apt update && apt upgrade -y && \
    apt install -y sshpass && \
    pip install -r requirements.txt

CMD python train.py && \
    python chats.py