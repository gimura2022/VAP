import log
import traceback
import json
import tts
import sst
import random
import datetime
import webbrowser
import os

try:
    with open("config.json",encoding="UTF-8") as file_config:config = json.load(file_config)

    tts.play(f"добрый день {config['name']}")

    date = datetime.datetime.now()

    if str(date.date())[5:] == config["date"]:tts.play("с днём рождения")

    def max2(z):
        log.file_log("start func max2")
        s = 0
        b = 0
        for x in range(len(z)):
            if z[x] > s:
                s = z[x]
                b = x
        return b

    def command(func,cmd):
        if sst.cmd.lower()[:len(cmd)] != "":
            if sst.cmd.lower()[:len(cmd)] == cmd:func()

    def command_end(func,cmd):
        if sst.cmd.lower()[:len(cmd)] != "":
            if sst.cmd.lower()[:len(cmd)] == cmd:func()
            else:log.file_log(f"{sst.cmd} not recognized as a command!")

    # здесь писать функции команд
    def time_func():
        tts.play(f"московское время {date.hour} часов {date.minute} минут")

    def help_func():
        tts.play("я могу отвечать на вопросы и помогать людям")

    def name_func():
        tts.play("меня зовут инакентий")

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
        tts.play("хорошо открываю")

        webbrowser.open(config["open_web"])

    def seath_web_func():
        tts.play("начинаю поиск")

        webbrowser.open(f"https://www.google.com/search?q={sst.cmd.split()[5:]}")

    # тут не трогать
    while True:
            sst.audio_ubdite()

            # тут писать вызовы команд
            command(time_func,f"кеша {config['command']['cmd_3'][0]}")
            command(time_func,f"кеша {config['command']['cmd_3'][1]}")
            command(time_func,f"кеша {config['command']['cmd_3'][2]}")

            command(help_func,f"кеша {config['command']['cmd_help'][0]}")
            command(help_func,f"кеша {config['command']['cmd_help'][1]}")
            command(help_func,f"кеша {config['command']['cmd_help'][2]}")

            command(name_func,f"кеша {config['command']['cmd_name'][0]}")

            command(web_func,f"кеша {config['command']['cmd_web'][0]}")
            command(web_func,f"кеша {config['command']['cmd_web'][1]}")

            command(seath_web_func,f"кеша {config['command']['cmd_web_seah'][0]}")
            command_end(seath_web_func,f"кеша {config['command']['cmd_web_seah'][1]}")

except:
    if config["debug"]:log.file_log(f"Error:\n{traceback.format_exc()}")
    else:log.file_log("Error")