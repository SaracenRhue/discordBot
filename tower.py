from os import system as cmd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import yaml

with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)
    USER = data['username']
    PASS = data['password']

TOWER = 'http://192.168.178.132'


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

# get metadata for stash from hqporner
def tag_hqporner():
    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
        USER = data['username']
        PASS = data['password']

    stash_url = "http://192.168.178.132:3069/scenes?c={%22type%22:%22url%22,%22value%22:%22%22,%22modifier%22:%22IS_NULL%22}&c={%22type%22:%22studios%22,%22value%22:{%22items%22:[{%22id%22:%2239%22,%22label%22:%22HQPorner%22}],%22depth%22:0},%22modifier%22:%22INCLUDES%22}&disp=1&perPage=1&sortby=created_at&sortdir=desc"
    site_url = "https://hqporner.com/?q="

    def createUrl(file_name):
        file_name = str(file_name)
        file_name = file_name.replace("Go to alternative player Loading may take some time ... ", "")
        file_name = file_name.replace(".mp4", "")
        file_name = file_name.replace(".mkv", "")
        file_name = file_name.replace("?", "")
        file_name = file_name.replace("!", "")
        file_name = file_name.replace("HQporner.com", "")
        file_name = file_name.replace(" -", "")
        file_name = file_name.replace(",", "")
        file_name = file_name.replace(" ", "+")
        return site_url + file_name

    driver = webdriver.Firefox()
    driver.get(stash_url)
    sleep(1)
    driver.find_element(by=By.ID, value='username').send_keys(USER)
    driver.find_element(by=By.ID, value='password').send_keys(PASS)
    driver.find_element(by=By.CLASS_NAME, value='btn').click()
    driver.get(stash_url)
    sleep(1)
    file_name = driver.find_element(By.TAG_NAME, value="h5").text
    driver.get(createUrl(file_name))
    sleep(1)
    title = driver.find_element(By.CLASS_NAME, value="meta-data-title")
    video_url = title.find_element(By.TAG_NAME, value="a").get_attribute("href")
    sleep(0.5)
    driver.get(stash_url)
    sleep(1)
    video_cards = driver.find_elements(by=By.TAG_NAME, value="td")
    video_cards[1].click()
    sleep(1)
    menu = driver.find_element(By.CLASS_NAME, value="nav-tabs")
    edit = menu.find_elements(By.CLASS_NAME, value="nav-link")[5]
    edit.click()
    url_input = driver.find_element(By.ID, value="url")
    url_input.send_keys(video_url)
    driver.find_element(By.CLASS_NAME, value="input-group-append").click()
    sleep(1)
    apply = driver.find_elements(By.TAG_NAME, value="button")
    apply[len(apply)-1].click()
    sleep(1)
    save = driver.find_element(By.CLASS_NAME, value="edit-button")
    save.click()
    sleep(0.5)
    driver.close()
    cmd('pkill firefox')

##################################################################

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

##################################################################
 


