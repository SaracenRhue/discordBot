log = []
def check(keyword):
    if len(log) >= 4:
        log = []
    for text in log:
        if 'new project' in text:
            return True
    return False
    




