from os import system as cmd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import yaml

with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)
    USER = data['toweruser']
    PASS = data['password']

TOWER = 'http://192.168.178.132'

## toggle gaming vm
def toggle_vm():
    driver = webdriver.Firefox()
    driver.get(TOWER)
    sleep(1)
    # login
    driver.find_elements(by=By.TAG_NAME, value='input')[0].send_keys(USER)
    driver.find_elements(by=By.TAG_NAME, value='input')[1].send_keys(PASS)
    driver.find_elements(by=By.TAG_NAME, value='button')[0].click()
    #switch to virtual machines
    driver.get(TOWER+'/VMs')
    sleep(1)
    # open vm dropdown
    vm_icon = driver.find_elements(by=By.TAG_NAME, value='img')[3]
    vm_icon.click()
    sleep(1)
    # toggle vm
    toggle_icon = driver.find_elements(by=By.TAG_NAME, value='li')[6]
    toggle_icon.click()
    # close browser
    driver.close()
    cmd('pkill firefox')

########################################################


# execute shell command
def use_shell(command):
    PATH = '/mnt/user'
    driver = webdriver.Firefox()
    driver.get(TOWER)
    # login
    driver.find_elements(by=By.TAG_NAME, value='input')[0].send_keys(USER)
    driver.find_elements(by=By.TAG_NAME, value='input')[1].send_keys(PASS)
    driver.find_elements(by=By.TAG_NAME, value='button')[0].click()
    #switch to terminal
    sleep(0.5)
    driver.get(TOWER+'/webterminal/ttyd/')
    sleep(1)
    terminal = driver.find_element(by=By.TAG_NAME, value='textarea')
    terminal.send_keys('cd '+PATH)
    terminal.send_keys('\n')
    terminal.send_keys(command)
    terminal.send_keys('\n')
    sleep(5)
    driver.close()
    cmd('pkill firefox')

###################################################

# get a random video url from stash
def random_stash_video():
    stash_url = 'http://192.168.178.132:3069/scenes?disp=1&perPage=1&sortby=random&sortdir=desc'

    driver = webdriver.Firefox()
    driver.get(stash_url)
    sleep(1)
    driver.find_element(by=By.ID, value='username').send_keys(USER)
    driver.find_element(by=By.ID, value='password').send_keys(PASS)
    driver.find_element(by=By.CLASS_NAME, value='btn').click()
    driver.get(stash_url)
    sleep(1)
    driver.find_element(By.TAG_NAME, value="h5").click()
    sleep(1)
    menu = driver.find_element(By.CLASS_NAME, value="nav-tabs")
    info = menu.find_elements(By.CLASS_NAME, value="nav-link")[4]
    info.click()
    sleep(1)
    links = driver.find_elements(By.TAG_NAME, value="a")
    for link in links:
        link = link.get_attribute("href")
        if link.__contains__("/scene/"):
            video_url = link
    driver.close()
    cmd('pkill firefox')

    return str(video_url)

###################################################

# reinstall code-server 
def inst_codeserver():
    driver = webdriver.Firefox()
    driver.get(TOWER)
    # login
    driver.find_elements(by=By.TAG_NAME, value='input')[0].send_keys(USER)
    driver.find_elements(by=By.TAG_NAME, value='input')[1].send_keys(PASS)
    driver.find_elements(by=By.TAG_NAME, value='button')[0].click()
    #switch to terminal
    sleep(0.5)
    driver.get(TOWER+'/logterminal/code-server/')
    sleep(1)
    terminal = driver.find_element(by=By.TAG_NAME, value='textarea')
    terminal.send_keys('bash -c "$(curl -fsSL https://raw.githubusercontent.com/SaracenRhue/unraidScripts/main/codeserver.sh)"')
    terminal.send_keys('\n')



