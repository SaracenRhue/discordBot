from os import system as cmd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import yaml

with open('secrets.yml', 'r') as file:
    data = yaml.safe_load(file)
    USER = data['username']
    PASS = data['password']
    TOWER = data['tower_ip']


# execute shell command
def use_shell(command):
    PATH = '/mnt/user'
    op = webdriver.FirefoxOptions()
    op.add_argument('--headless')
    driver = webdriver.Firefox(options=op)
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

# reinstall code-server 
def inst_codeserver():
    op = webdriver.FirefoxOptions()
    op.add_argument('--headless')
    driver = webdriver.Firefox(options=op)
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

##################################################################
 


