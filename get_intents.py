import yaml
import json
import os

# combine all files in intents folder into one file

intents = {'intents':[]}
for file in os.listdir('intents'):
    with open(f'intents/{file}', 'r') as f:
        file = yaml.safe_load(f)
        for item in file:
            intents['intents'].append(item)

with open('intents.json', 'w+') as f:
    json.dump(intents, f)
