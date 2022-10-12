import discord
import yaml
import tower



with open('data.yml', 'r') as f:
    data = yaml.safe_load(f)
    TOKEN = data['token']

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  mgs = message.content.lower()
  if message.author == client.user:
    return

  if mgs.startswith('hello'):
    await message.channel.send('hi')
  elif mgs.startswith('$'):
    tower.use_shell(mgs[1:])
  elif 'vm' in mgs:
    tower.toggle_vm()
    await message.channel.send('on it')
  elif 'porn' in mgs:
    await message.channel.send('on it')
    await message.channel.send(tower.random_stash_video())
  elif 'vsc' in mgs:
    tower.inst_codeserver()
    await message.channel.send('on it')

client.run(TOKEN)
