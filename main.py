import discord
import yaml
import openai
import tower
import chat
import ssh
import os



with open('secrets.yml', 'r') as f:
    data = yaml.safe_load(f)
    TOKEN = data['token']
    OPENAI = data['openai']
    ADMIN = data['bot_admin']


def check_author(message):
    if message.author == client.user and str(message.author) != ADMIN:
      return False

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if check_author(message) == False:
    return

  mgs = message.content.lower()

 # await ssh.check(message)

  openai.api_key = OPENAI
  
  # Use the `openai.Completion.create()` method to generate text
  prompt = (mgs)
  completions = openai.Completion.create(
      engine='text-davinci-002',
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )
  await message.channel.send(completions.choices[0].text)


client.run(TOKEN)
