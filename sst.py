import speech_recognition as sr
import log

log.file_log("creating variables")

r = sr.Recognizer()
cmd = ""

def audio_ubdite():
    global cmd

    log.file_log("Start func audio_ubdate")

    with sr.Microphone() as source:audio_ = r.listen(source)

    try:
        log.file_log(f"первичное распознование: {r.recognize_google(audio_, language='ru-RU').lower()}")

        cmd = r.recognize_google(audio_, language="ru-RU").lower()

    except sr.UnknownValueError:log.file_log("фраза не распознана!")

    except sr.RequestError as servis:log.file_log(f"Error servis sst {servis}")