import discord
import yaml
import tower
import chat
import history
import generator as gen



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

  history.add_msg(mgs)
  print(history.log)
  # if 'new' and 'project' and 'c++' or 'cpp' or 'python' or 'docker' in history.log:
  #   history.log = []
  #   history.log.append('project_name')
  #   if 'c++' or 'cpp' in history.log:
  #     await chat.send('c++', message)
  #     return
  #   elif 'python' in history.log:
  #     await chat.send('python', message)
  #     return
  #   elif 'docker' in history.log:
  #     await chat.send('docker', message)
  #     return

  # elif 'new'and 'project' in history.log:
  #   await chat.send('what type of project do you want to make?', message)
  #   return


  if mgs.startswith('hello') or mgs.startswith('hi'):
    await chat.rnd('greeting', message)
  elif mgs.startswith('$'):
    tower.use_shell(mgs[1:])
  elif 'vm' in mgs:
    tower.toggle_vm()
    await chat.rnd('working', message)
  elif 'hqporner' in mgs:
    tower.tag_hqporner()
    await chat.rnd('working', message)
  elif 'porn' in mgs:
    await chat.rnd('working', message)
    await chat.send(tower.random_stash_video(), message)
  elif 'vsc' in mgs:
    tower.inst_codeserver()
    await chat.rnd('working', message)
  # elif 'new' and 'project' in history.log:
  #   type = history.log[1]
  #   name = history.log[-1]
  #   gen.create_pro(name, type)

  history.log.clear()

    
client.run(TOKEN)
