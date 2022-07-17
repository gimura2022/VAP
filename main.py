try:import log

except:pass
import log
import traceback

excepts = ""

try:
    import json

    with open("config.json",encoding="UTF-8") as file_config:config = json.load(file_config)

except:
    if config["tester"]:log.file_log(f"Error:\n{traceback.format_exc()}");config = None

    else:excepts += "3,";config = None

try:
    import tts
    import sst
    import random
    from fuzzywuzzy import fuzz
    import datetime
    import webbrowser
    import os

except:
    if config["tester"]:log.file_log(f"Error:\n{traceback.format_exc()}")

    else:excepts += "2,"

try:
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

    def fuzz_cmd(_1,_2):
        try:return fuzz.ratio(_1,_2)

        except:return 0

    def ceha(num):
            log.file_log("start func ceha")
        
            log.file_log("command description...")

            # время
            cmd_3 = fuzz_cmd(config["command"]["cmd_3"][0], sst.cmd[len(config["name_"][num]):])

            cmd_3_1 = fuzz_cmd(config["command"]["cmd_3"][1], sst.cmd[len(config["name_"][num]):])

            cmd_3_2 = fuzz_cmd(config["command"]["cmd_3"][2], sst.cmd[len(config["name_"][num]):])

            # стоп
            cmd_stop = fuzz_cmd(config["command"]["cmd_stop"][0], sst.cmd[len(config["name_"][num]):])

            # анегдот
            cmd_a_0 = fuzz_cmd(config["command"]["cmd_a"][0], sst.cmd[len(config["name_"][num]):])
            cmd_a_1 = fuzz_cmd(config["command"]["cmd_a"][1], sst.cmd[len(config["name_"][num]):])
            cmd_a_2 = fuzz_cmd(config["command"]["cmd_a"][2], sst.cmd[len(config["name_"][num]):])

            # помошь
            cmd_help = fuzz_cmd(config["command"]["cmd_help"][0], sst.cmd[len(config["name_"][num]):])
            cmd_help_1 = fuzz_cmd(config["command"]["cmd_help"][1], sst.cmd[len(config["name_"][num]):])
            cmd_help_2 = fuzz_cmd(config["command"]["cmd_help"][2], sst.cmd[len(config["name_"][num]):])

            # рандомное число
            cmd_rand_0 = fuzz_cmd(config["command"]["cmd_rand"][0], sst.cmd[len(config["name_"][num]):])
            cmd_rand_1 = fuzz_cmd(config["command"]["cmd_rand"][1], sst.cmd[len(config["name_"][num]):])

            # как дела
            cmd_k_0 = fuzz_cmd(config["command"]["cmd_k"][0], sst.cmd[len(config["name_"][num]):])
            cmd_k_1 = fuzz_cmd(config["command"]["cmd_k"][1], sst.cmd[len(config["name_"][num]):])

            # как тебя зовут
            cmd_name_0 = fuzz_cmd(config["command"]["cmd_name"][0], sst.cmd[len(config["name_"][num]):])
            cmd_name_1 = fuzz_cmd(config["command"]["cmd_name"][1], sst.cmd[len(config["name_"][num]):])

            # сегоднешняя дата
            cmd_data_0 = fuzz_cmd(config["command"]["cmd_date"][0], sst.cmd[len(config["name_"][num]):])
            cmd_data_1 = fuzz_cmd(config["command"]["cmd_date"][1], sst.cmd[len(config["name_"][num]):])
            cmd_data_2 = fuzz_cmd(config["command"]["cmd_date"][2], sst.cmd[len(config["name_"][num]):])

            # браузер
            cmd_web_0 = fuzz_cmd(config["command"]["cmd_web"][0], sst.cmd[len(config["name_"][num]):])
            cmd_web_1 = fuzz_cmd(config["command"]["cmd_web"][1], sst.cmd[len(config["name_"][num]):])

            # поиск
            cmd_web_seah_0 = fuzz_cmd(config["command"]["cmd_web_seah"][0], sst.cmd[len(config["name_"][num]):len(config["command"]["cmd_web_seah"][0])])
            cmd_web_seah_1 = fuzz_cmd(config["command"]["cmd_web_seah"][1], sst.cmd[len(config["name_"][num]):len(config["command"]["cmd_web_seah"][1])])

            # поиск в ютуб
            cmd_youtube_0 = fuzz_cmd(config["command"]["cmd_youtube"][0], sst.cmd[len(config["name_"][num]):len(config["command"]["cmd_youtube"][0])])
            cmd_youtube_1 = fuzz_cmd(config["command"]["cmd_youtube"][1], sst.cmd[len(config["name_"][num]):len(config["command"]["cmd_youtube"][1])])

            #выключение
            cmd_off = fuzz_cmd(config["command"]["cmd_off"][0], sst.cmd[len(config["name_"][num]):])

            log.file_log(f"cmd_3: {cmd_3}%")
            log.file_log(f"cmd_3_1: {cmd_3_1}%")
            log.file_log(f"cmd_3_2: {cmd_3_2}%")
            log.file_log(f"cmd_stop: {cmd_stop}%")
            log.file_log(f"cmd_a_0: {cmd_a_0}%")
            log.file_log(f"cmd_a_1: {cmd_a_1}%")
            log.file_log(f"cmd_a_2: {cmd_a_2}%")
            log.file_log(f"cmd_help: {cmd_help}%")
            log.file_log(f"cmd_help_1: {cmd_help_1}%")
            log.file_log(f"cmd_help_2: {cmd_help_2}%")
            log.file_log(f"cmd_rand_0: {cmd_rand_0}%")
            log.file_log(f"cmd_rand_1: {cmd_rand_1}%")
            log.file_log(f"cmd_k_0: {cmd_k_0}%")
            log.file_log(f"cmd_k_1: {cmd_k_1}%")
            log.file_log(f"cmd_name_0: {cmd_name_0}%")
            log.file_log(f"cmd_name_1: {cmd_name_1}%")
            log.file_log(f"cmd_data_0: {cmd_data_0}%")
            log.file_log(f"cmd_data_1: {cmd_data_1}%")
            log.file_log(f"cmd_data_2: {cmd_data_2}%")
            log.file_log(f"cmd_web_0: {cmd_web_0}%")
            log.file_log(f"cmd_web_1: {cmd_web_1}%")
            log.file_log(f"cmd_web_seah_0: {cmd_web_seah_0}%")
            log.file_log(f"cmd_web_seah_1: {cmd_web_seah_1}%")
            log.file_log(f"cmd_youtube_0: {cmd_youtube_0}%")
            log.file_log(f"cmd_youtube_1: {cmd_youtube_1}%")
            log.file_log(f"cmd_off: {cmd_off}%")

            #        0       1       2       3       4      5      6           7          8           9        10         11        12      13      14           15        16           17        18     19        20         21               22            23         24            25
            cmd = [cmd_3,cmd_3_1,cmd_3_2,cmd_a_0,cmd_a_1,cmd_a_2,cmd_data_0,cmd_data_1,cmd_data_2,cmd_help,cmd_help_1,cmd_help_2,cmd_k_0,cmd_k_1,cmd_name_0,cmd_name_1,cmd_rand_0,cmd_rand_1,cmd_stop,cmd_web_0,cmd_web_1,cmd_web_seah_0,cmd_web_seah_1,cmd_youtube_0,cmd_youtube_1,cmd_off]

            cmd_otv = max2(cmd)

            log.file_log(f"наиболее вероятный ответ: '{cmd_otv}' вероятность того что он верен равна: {cmd[cmd_otv]}%") 

            if cmd[cmd_otv] >= config["t"]:
                # время
                if cmd_otv == 0 or cmd_otv == 1 or cmd_otv == 2:
                        log_time = datetime.datetime.now()
                        tts.play(f"московское время {log_time.hour} часов {log_time.minute} минут")
                        start()

                # стоп
                elif cmd_otv == 18:
                    tts.play("выключение")
                    log.file_log("stop!")

                # анегдот
                elif cmd_otv == 3 or cmd_otv == 4 or cmd_otv == 5:
                    tts.play(config["command"]["cmd_a_otv"][random.randint(0,1)])
                    start()

                # помощь
                elif cmd_otv == 9 or cmd_otv == 10 or cmd_otv == 11:
                    tts.play("я умею шутить узнавать время генерировать случаные числа и отвечать на вопросы")
                    start()

                # рандомное число
                elif cmd_otv == 16 or cmd_otv == 17:
                    tts.play(random.randint(1,100))
                    start()

                # как дела
                elif cmd_otv == 12 or cmd_otv == 13:
                    tts.play("хорошо но никто не завидует")
                    start()

                # как тебя зовут
                elif cmd_otv == 14 or cmd_otv == 15:
                    tts.play(f"меня зовут {config['name_'][0]}")
                    start()

                # сегодняшняя дата
                elif cmd_otv == 6 or cmd_otv == 7 or cmd_otv == 8:
                    date = datetime.datetime.now()

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
                    start()

                # браузер
                elif cmd_otv == 19 or cmd_otv == 20:
                    tts.play("хорошо")

                    webbrowser.open_new_tab("https://www.google.com/")

                    start()

                # поиск
                elif cmd_otv == 21 or cmd_otv == 22:
                    tts.play(f"ищу ответ в интернете по запросу {sst.cmd[len(config['command']['cmd_web_seah'][0])+(len(config['name_'][num])+1):]}")

                    webbrowser.open_new_tab(f"https://www.google.com/search?q={sst.cmd[len(config['command']['cmd_web_seah'][0])+(len(config['name_'][num])+1):]}")

                    start()

                # youtube
                elif cmd_otv == 23 or cmd_otv == 24:
                    tts.play(f"ищу ответ в ютубе по запросу {sst.cmd}")

                    webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={sst.cmd[len(config['command']['cmd_youtube'][0])+(len(config['name_'][num])+1):]}")

                    start()

                # выключение
                elif cmd_otv == 25:
                    tts.play("хорошо выключение")
                    
                    os.system('shutdown /p /f')

                    log.file_log("stop system")
                    
                # команда не распознана!
                else:
                    log.file_log("команда не распознана!")
                    start()

            else:start()

    def start():
        log.file_log("start func Start")

        sst.audio_ubdite()

        name_k = fuzz.ratio(config["name_"][0], sst.cmd[:len(config["name_"][0])])
        name_k_1 = fuzz.ratio(config["name_"][1], sst.cmd[:len(config["name_"][0])])
        name_k_2 = fuzz.ratio(config["name_"][2], sst.cmd[:len(config["name_"][0])])

        log.file_log(f"name_k: {name_k}%")
        log.file_log(f"name_k_1: {name_k_1}%")
        log.file_log(f"name_k_2: {name_k_2}%")

        cmd_ = [name_k,name_k_1,name_k_2]

        cmd_otv_ = max2(cmd_)

        log.file_log(f"наиболее вероятный ответ: {cmd_otv_} вероятность того что он верен равна: {cmd_[cmd_otv_]}%")

        if cmd_[cmd_otv_] >= config["t"]:
            if cmd_otv_ == 0:
                log.file_log("вызов Кеши")
                ceha(0)

            elif cmd_otv_ == 1:
                log.file_log("вызов Кеши")
                ceha(1)

            elif cmd_otv_ == 2:
                log.file_log("вызов Кеши")
                ceha(2)

            else:start()

        else:start()

    start()

except:
    if config["tester"]:log.file_log(f"Error:\n{traceback.format_exc()}")

    else:excepts += "1,"

finally:log.file_log(f"exit codes {excepts[:-1] if excepts != '' else None}" if len(excepts[:-1]) > 1 else f"exit code {excepts[:-1] if excepts != '' else None}")