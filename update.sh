#!/bin/bash

cd
mv discordbot/secrets.yml .
rm -fr discordbot
git clone https://github.com/SaracenRhue/discordbot.git
mv secrets.yml ./discordbot
cd discordbot
python3 ./main.py
