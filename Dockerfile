FROM python:3.10-slim

WORKDIR /home/app

COPY . .

RUN apt update && apt upgrade -y && \
    apt install -y sshpass g++ && \
    pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# VOLUME /home/app/secure

CMD python get_intents.py && \
    python train.py && \
    python chats.py