import yaml
from os import system as cmd
import utils
from pyllamacpp.model import Model

def send_command(command):
    """Send a command to the server via ssh"""
    cmd(f'sshpass -p {PASSWORD} ssh {USER}@{IP} "{command}"')

with open('secure/secrets.yml', 'r') as f:
    SECRETS = yaml.safe_load(f)
    USER = SECRETS['user']
    PASSWORD = SECRETS['password']
    IP = SECRETS['tower_ip']

def check_intent(intent : str, message : str):
    """Check if the intent has a matching action"""
    match intent:
        case 'goodbye':
            return send_command('docker stop discordbot') 
        case 'start windows':
            return send_command('virsh start Windows\ 11')
        case 'stop windows':
            return send_command('virsh stop Windows\ 11')
        case 'start plex':
            return send_command('docker start plex')
        case 'stop plex':
            return send_command('docker stop plex')
        case 'restart plex':
            return send_command('docker restart plex')
        case 'start sabnzb':
            return send_command('docker start binhex-sabnzbdvpn')
        case 'stop sabnzb':
            return send_command('docker stop binhex-sabnzbdvpn')
        case 'restart sabnzb':
            return send_command('docker restart binhex-sabnzbdvpn')
        case 'start stable diffusion':
            return send_command('docker start stable-diffusion')
        case 'stop stable diffusion':
            return send_command('docker stop stable-diffusion')
        case 'restart stable diffusion':
            return send_command('docker restart stable-diffusion')
        case 'start nginx':
            return send_command('docker start NginxProxyManager')
        case 'stop nginx':
            return send_command('docker stop NginxProxyManager')
        case 'restart nginx':
            return send_command('docker restart NginxProxyManager')
        case 'unknown':
            model = Model(ggml_model='./gpt4all-converted.bin', n_ctx=512)
            generated_text = model.generate("Once upon a time, ", n_predict=55)
            print(generated_text)