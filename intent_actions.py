import yaml
from os import system as cmd

def send_command(command):
    cmd(f'sshpass -p {PASSWORD} ssh {USER}@{IP} "{command}"')

with open('secrets.yml', 'r') as f:
    SECRETS = yaml.safe_load(f)
    USER = SECRETS['user']
    PASSWORD = SECRETS['password']
    IP = SECRETS['tower_ip']

def check_intent(intent):
    match intent:
        case 'start windows':
            send_command('virsh start Windows\ 11')
        case 'stop windows':
            send_command('virsh stop Windows\ 11')
        case 'start plex':
            send_command('docker start plex')
        case 'stop plex':
            send_command('docker stop plex')
        case 'restart plex':
            send_command('docker restart plex')
        case 'start sabnzb':
            send_command('docker start binhex-sabnzbdvpn')
        case 'stop sabnzb':
            send_command('docker stop binhex-sabnzbdvpn')
        case 'restart sabnzb':
            send_command('docker restart binhex-sabnzbdvpn')
        case 'start stable diffusion':
            send_command('docker start stable-diffusion')
        case 'stop stable diffusion':
            send_command('docker stop stable-diffusion')
        case 'restart stable diffusion':
            send_command('docker restart stable-diffusion')
        case 'start nginx':
            send_command('docker start NginxProxyManager')
        case 'stop nginx':
            send_command('docker stop NginxProxyManager')
        case 'restart nginx':
            send_command('docker restart NginxProxyManager')
        case _:
            pass