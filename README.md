# discord-bot

## dependencies

```bash
sudo apt install python3 python3-pip sshpass
pip3 install discord pyyaml selenium pyautogui
```

## setup

Add a secrets.yml file with the following structure:

```yml
token: your discord bot token
bot_admin: your discord username#id
toweruser: your tower root user
username: your container username
password: password
tower_ip: http://tower_ip

ssh:
  mac: 
    login: user@ip
    password: password
  tower:
    login: root_user@ip
    password: password
```
