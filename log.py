import datetime
import json

with open("config\\sesion.json") as f:
    sesion = json.load(f)

with open("config\\sesion.json","w") as f:
    f.write(json.dumps(sesion + 1))

with open("config\\config.json") as config_file:
    config = json.load(config_file)

def file_log(data):
    if config["loging"]:
        with open(f"log\\{sesion}.log","a",encoding='UTF-8') as f:
            f.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}]{data}\n")

    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}]{data}")