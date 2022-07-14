from datetime import datetime
from json import load,dumps
from os import mkdir

try:
    with open("config\\sesion.json") as f:sesion = load(f)

except:
    with open("config\\sesion.json","w+") as f:f.write(dumps(0));sesion = load(f)

with open("config\\sesion.json","w") as f:f.write(dumps(sesion + 1))

with open("config\\config.json") as config_file:config = load(config_file)

def file_log(data):
    if config["loging"]:
        try:
            with open(f"log\\{sesion}.log","a",encoding='UTF-8') as f:f.write(f"[{datetime.now().strftime('%H:%M:%S')}]{data}\n")

        except:
            mkdir("log")
            with open(f"log\\{sesion}.log","a",encoding='UTF-8') as f:f.write(f"[{datetime.now().strftime('%H:%M:%S')}]{data}\n")

    print(f"[{datetime.now().strftime('%H:%M:%S')}]{data}")