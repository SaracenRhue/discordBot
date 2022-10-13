import yaml
import random

with open('chat.yml', 'r') as f:
    data = yaml.safe_load(f)

def rnd_txt(key):
    return random.choice(data[key])
