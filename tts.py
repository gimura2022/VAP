import log
import pyttsx3
import json

with open("config\\config.json",encoding="UTF-8") as file_config:
    config = json.load(file_config)

def play(data):
    log.file_log("start func play")
    log.file_log(f"play: {data}")

    s = pyttsx3.init()

    voices = s.getProperty('voices')
    s.setProperty('voice', voices[config["model_tts"]].id)

    s.say(str(data)) 
    s.runAndWait()