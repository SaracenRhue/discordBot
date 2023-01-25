from os import system as cmd
import yaml

with open('secrets.yml', 'r') as f:
    data = yaml.safe_load(f)
    TOWER_LOGIN = data['ssh']['tower']['login']
    TOWER_PASSWORD = data['ssh']['tower']['password']
with open('data.yml', 'r') as f:
    data = yaml.safe_load(f)
    CONTAINERS = data['containers']
    VMS = data['vms']



def into_tower(command):
    send(TOWER_LOGIN, TOWER_PASSWORD, command)

def send(host, password, command):
    cmd(f"sshpass -p '{password}' ssh {host} '{command}'")

def start_container(container):
    return f"docker start {container}"

def stop_container(container):
    return f"docker stop {container}"

def start_vm(vm):
    return f"virsh start {vm}"

def stop_vm(vm):
    return f"virsh shutdown {vm}"


async def check(message):
    mgs = message.content.lower()
    if 'start' in mgs:
        for container in CONTAINERS:
            if container in mgs:
                into_tower(start_container(data['containers'][container]['name']))
                await message.channel.send(f"Started {container}")
                return
        for vm in VMS:
            if vm in mgs:
                into_tower(start_vm(data['vms'][vm]['name']))
                await message.channel.send(f"Started {vm}")
                return
    elif 'stop' in mgs:
        for container in CONTAINERS:
            if container in mgs:
                into_tower(stop_container(data['containers'][container]['name']))
                await message.channel.send(f"Stopped {container}")
                return
        for vm in VMS:
            if vm in mgs:
                into_tower(stop_vm(data['vms'][vm]['name']))
                await message.channel.send(f"Stopped {vm}")
                return
