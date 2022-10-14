log = []
def add_msg(msg):
    for word in msg.split():
        log.append(word)

def check(keyword):
    for text in log:
        if 'new project' in text:
            return True
    return False
    
def clear():
    global log
    log = []



