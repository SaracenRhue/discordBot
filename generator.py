import yaml
import ssh


with open('generator_config.yml', 'r') as file:
    config = yaml.safe_load(file)
    projects = config['projects']
    main_path = config['main_path']


def create_pro(name, type):
    pro_name = name
    pro_type = type
    pro_type = projects.get(pro_type) 

    path = main_path + pro_type['path']
    create_cmd = pro_type['cmd']
    create_cmd = create_cmd.replace('pro_name', pro_name)

    ssh.into_mac(f'cd {path} && {create_cmd}')

    if 'github' in create_cmd:
        ssh.into_mac(f'cd && rm -rf {path}{pro_name}/LICENSE') #remove license file


