import discord
import yaml
import tower
import chat
import history


with open('data.yml', 'r') as f:
    data = yaml.safe_load(f)
    TOKEN = data['token']
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
  history.log.append(mgs)
  if mgs.startswith('hello') or mgs.startswith('hi'):
    await message.channel.send(chat.rnd_txt('greeting'))
  elif mgs.startswith('$'):
    tower.use_shell(mgs[1:])
  elif 'vm' in mgs:
    tower.toggle_vm()
    await message.channel.send(chat.rnd_txt('working'))
  elif 'porn' in mgs:
    await message.channel.send(chat.rnd_txt('working'))
    await message.channel.send(tower.random_stash_video())
  elif 'vsc' in mgs:
    tower.inst_codeserver()
    await message.channel.send(chat.rnd_txt('working'))

client.run(TOKEN)
