import random
import string
import re

def get_random_string(len):
    return ''.join((random.choice(string.ascii_letters + string.digits) for i in range(len)))

def validate_password(password):
    msg = ''
    if len(password) < 8:
        msg += "Password must contain least 8 characters!   "
    if re.search('[0-9]',password) is None:
        msg += "Password must contain a number!   "
    if re.search('[a-z]',password) is None:
        msg += "Password must contain a lowercase letter!   "
    if re.search('[A-Z]',password) is None: 
        msg += "Password must contain a uppercase letter!   "
    return msg