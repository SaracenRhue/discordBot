import yaml
import random
import discord

with open('chat.yml', 'r') as f:
    data = yaml.safe_load(f)


async def send(text, message):
    await message.channel.send(text)

async def sendf(file_path, message):
    await message.channel.send(file=discord.File(file_path))

async def rnd(key, message):
    await message.channel.send(random.choice(data[key]))