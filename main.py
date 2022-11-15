import log
import traceback
import json
import tts
import sst
import random
import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup

try:
    with open("config.json",encoding="UTF-8") as file_config:config = json.load(file_config)

    with open("web_tabs.json",encoding="UTF-8") as file_tabs:tabs = json.load(file_tabs)

    date = datetime.datetime.now()

    if date.hour >= 0 and date.hour <= 12:date_str = "доброе утро"
    elif date.hour > 12 and date.hour <= 18:date_str = "добрый день"
    else:date_str = "добрый вечер"

    tts.play(f"{date_str} {config['name']}")

    if str(date.date())[5:] == config["date"]:tts.play(f"с днём рождения {config['name']}")

    def max2(z):
        log.file_log("start func max2")
        s = 0
        b = 0
        for x in range(len(z)):
            if z[x] > s:
                s = z[x]
                b = x
        return b

    # здесь писать функции команд
    def time_func():
        tts.play(f"московское время {date.hour} часов {date.minute} минут")

    def date_func():
        month = ""

        if date.month == 1:
            month = "января"

        elif date.month == 2:
            month = "февраля"

        elif date.month == 3:
            month = "марта"

        elif date.month == 4:
            month = "апреля"

        elif date.month == 5:
            month = "мая"

        elif date.month == 6:
            month = "июня"

        elif date.month == 7:
            month = "июля"

        elif date.month == 8:
            month = "августа"

        elif date.month == 9:
            month = "сентября"

        elif date.month == 10:
            month = "октября"

        elif date.month == 11:
            month = "ноября"

        elif date.month == 12:
            month = "декабря"

        tts.play(f"сейчас {date.day} {month} {date.year} года")

    def web_func():
        webbrowser.open_new_tab(config["open_web"])

    # def seath_web_func():
    #     webbrowser.open(f"https://www.google.com/search?q={sst.cmd.split()[5:]}")

    def pogoda_func():
        url = 'https://pogoda.mail.ru/prognoz/moskva/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        b = soup.find('div', class_='information__content__temperature')
        
        tts.play(f"за окном {b.text.split()[0][1:-1]} градусов")

    def web_tabs(index):
        webbrowser.open_new_tab(tabs[index])

    # тут не трогать
    while True:
            sst.audio_ubdite()

            inp = []

            for i in range(len(sst.cmd.lower().split())):
                if sst.cmd.lower().split()[i] != "кеша":inp.append(sst.cmd.lower().split()[i])

            for i in range(len(config["command"])):
                for x in range(len(config["command"][i]["inp"])):
                    if config['command'][i]['inp'][x].split() == inp and "кеша" in sst.cmd.lower():
                        if config["command"][i]["out"] != None:tts.play(config["command"][i]["out"][random.randint(0,len(config["command"][i]["out"])-1)])
                        if config["command"][i]["func"] != None:
                            if config['command'][i]['args'] == None:exec(f"{config['command'][i]['func']}()")
                            else:exec(f"{config['command'][i]['func']}{config['command'][i]['args']}")

except:
    if config["debug"]:log.file_log(f"Error:\n{traceback.format_exc()}")
    else:log.file_log("Error")