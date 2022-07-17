from datetime import datetime
from json import load,dumps
from os import mkdir

try:
    with open("log\\sesion.json") as f:sesion = load(f)

except:
    try:mkdir("log")

    except:pass

    with open("log\\sesion.json","w+") as f:f.write(dumps(0));sesion = load(f)

with open("log\\sesion.json","w") as f:f.write(dumps(sesion + 1))

with open("config\\config.json") as config_file:config = load(config_file)

def file_log(data):
    if config["loging"]:
        with open(f"log\\{sesion}.log","a",encoding='UTF-8') as f:f.write(f"[{datetime.now().strftime('%H:%M:%S')}]{data}\n")

    print(f"[{datetime.now().strftime('%H:%M:%S')}]{data}")