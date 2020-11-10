import re

def check_pwd(pwd):         
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    if pwd.isdigit():
        return False
    if not re.search('[0-9]', pwd):
        return False    
    if not re.search('[a-z]', pwd):
        return False
    if not re.search('[A-Z]', pwd):
        return False

    return True