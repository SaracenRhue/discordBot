import random
import yaml
import torch
import discord

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from intent_actions import check_intent

def check_author(message):
    if message.author == client.user and str(message.author) != ADMIN:
      return False

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
client = discord.Client(intents=discord.Intents.default())


with open('intents.yml', 'r') as f:
    intents = yaml.safe_load(f)
with open('secrets.yml', 'r') as f:
    data = yaml.safe_load(f)
    TOKEN = data['token']
    ADMIN = data['bot_admin']

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Edith"
print("Let's chat! (type 'quit' to exit)")
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if check_author(message) == False:
    return

  mgs = message.content

  # sentence = "do you use credit cards?"
  sentence = mgs
   
  sentence = tokenize(sentence)
  X = bag_of_words(sentence, all_words)
  X = X.reshape(1, X.shape[0])
  X = torch.from_numpy(X).to(device)   
  output = model(X)
  _, predicted = torch.max(output, dim=1)  
  tag = tags[predicted.item()]     
  probs = torch.softmax(output, dim=1)
  prob = probs[0][predicted.item()]
  if prob.item() > 0.75:
      for intent in intents['intents']:
          if tag == intent["tag"]:
              check_intent(intent["tag"])
              await message.channel.send(f"{random.choice(intent['responses'])}")
              print(f'tag: {intent["tag"]}')
  else:
      await message.channel.send(f"I do not understand...")
    

client.run(TOKEN)