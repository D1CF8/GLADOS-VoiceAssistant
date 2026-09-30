import eel
import pyttsx3
import datetime
import webbrowser
from components import AI
from components import systemData as phrases
from components import mainSystem
from fuzzywuzzy import fuzz, process
import json

def TextCorect(text: str):
    text = text.lower()
    text_list = text.split()
    if (text_list[0] == "включи" and text_list[1] != "музыку") or text_list[0] in phrases.game_com or text_list[0] in phrases.search_com or text_list[0] in phrases.site_open_com:
        return [text, -1]
    else:
        match_time = list(process.extractOne(text, phrases.time_com, scorer=fuzz.token_sort_ratio))
        match_date = list(process.extractOne(text, phrases.data_com, scorer=fuzz.token_sort_ratio))
        match_music_on = list(process.extractOne(text, phrases.music_on_com, scorer=fuzz.token_sort_ratio))
        arr = [match_time, match_date, match_music_on]
        maxMatch = max(match_time[1], match_date[1], match_music_on[1])
        for i in arr:
            if i[1] == maxMatch and maxMatch >= 80:
                return i
    return [text, 0]
def Talk(text):
    prompt = f"Представь, что ты GLADOS из Portal 2. Ответь на высказывание или вопрос пользователя, или поговори с ним (на твоё усмотрение). Пользователь ввёл: {text} Не нужно издавать звуков по типу 'механический вздох'" \
             f"или 'радосный гудок' и тд, и без указания интонации. Мне нужно только сообщение"
    answer = str(AI.deepseek_chat(prompt)).replace("*", "")
    voice = pyttsx3.init()
    voice.say(answer)
    voice.runAndWait()

def Time():
    data = datetime.datetime.now()
    prompt = f"Представь, что ты GLADOS из Portal 2. Скажи время (без секунд), можешь использовать какой-нибудь комментарий или саркастическую шутку. Сейчас: {data}. НО ВРЕМЯ ТЫ ДОЛЖНА СКАЗАТЬ ОБЯЗАТЕЛЬНО и не нужно издавать звуков по типу 'механический вздох'" \
             f"или 'радосный гудок' и тд, и без указания интонации. Мне нужно только сообщение"
    answer = str(AI.deepseek_chat(prompt)).replace("*", "")
    voice = pyttsx3.init()
    voice.say(answer)
    voice.runAndWait()

def Data():
    data = datetime.datetime.now()
    prompt = f"Представь, что ты GLADOS из Portal 2. Скажи дату (без года), можешь использовать какой-нибудь комментарий или саркастическую шутку. Сейчас: {data}. НО ДАТУ ТЫ ДОЛЖНА СКАЗАТЬ ОБЯЗАТЕЛЬНО и не нужно издавать звуков по типу 'механический вздох'" \
             f"или 'радосный гудок' и тд, и без указания интонации. Мне нужно только сообщение"
    answer = str(AI.deepseek_chat(prompt)).replace("*", "")
    voice = pyttsx3.init()
    voice.say(answer)
    voice.runAndWait()

def Game_phrases(text):
    if mainSystem.Random_answer():
        prompt = f"Представь, что ты GLADOS из Portal 2. Пользователь хочет запустить каку-нибудь игру и тебе нужно что-то сказать по этому поводу, можешь использовать какой-нибудь комментарий или саркастическую шутку. Не нужно издавать звуков по типу 'механический вздох'" \
             f"или 'радосный гудок' и тд, и без указания интонации. Мне нужно только сообщение"
        answer = str(AI.deepseek_chat(prompt)).replace("*", "")
        voice = pyttsx3.init()
        voice.say(answer)
        voice.runAndWait()
    mainSystem.Game_start(text)

def Music_phrases(text = ""):
    if mainSystem.Random_answer():
        prompt = f"Представь, что ты GLADOS из Portal 2. Пользователь хочет включить каку-нибудь музыку и тебе нужно что-то сказать по этому поводу, можешь использовать какой-нибудь комментарий или саркастическую шутку. Не нужно издавать звуков по типу 'механический вздох'" \
             f"или 'радосный гудок' и тд, и без указания интонации. Мне нужно только сообщение"
        answer = str(AI.deepseek_chat(prompt)).replace("*", "")
        voice = pyttsx3.init()
        voice.say(answer)
        voice.runAndWait()
    mainSystem.Music_play(text)

def Search(text_list):
    text = ""
    for i in text_list:
        text += i
    if mainSystem.Random_answer():
        prompt = f"Представь, что ты GLADOS из Portal 2. Пользователь хочет может найти какую-то информацию, прокаментируй его запрос, можешь использовать какой-нибудь комментарий или саркастическую шутку. Запрос пользователя: {text}. Не нужно издавать звуков по типу 'механический вздох'" \
             f"или 'радосный гудок' и тд, и без указания интонации. Мне нужно только сообщение. Но НЕ В КОЕМ СЛУЧАЕ НЕ РЕШАЙ ЕГО ПРОБЛЕМУ, НАПИСАННУЮ В ЗАПРОСЕ, ПРОСТО ПРОКОМЕНТИРУЙ"
        answer = str(AI.deepseek_chat(prompt)).replace("*", "")
        voice = pyttsx3.init()
        voice.say(answer)
        voice.runAndWait()
    webbrowser.open(text.replace("/", "").replace("[", "").replace(",", "").replace("]", "").replace(":", "").replace("'", ""))


SETTINGS_FILE = phrases.jsonFile

def load_settings():
    if SETTINGS_FILE.exists():
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except Exception as e:
            return {"input_mode": "voice", "theme": "dark"}
    else:
        return {"input_mode": "voice", "theme": "dark"}

settings = load_settings()

@eel.expose
def get_settings(*args):
    return settings

@eel.expose
def save_settings(new_settings, *args):
    global settings
    if new_settings == "voice" or new_settings == "text":
        data = {
            "input_mode": new_settings,
            "theme": settings['theme']
        }
    else:
        data = {
            "input_mode": settings['input_mode'],
            "theme": new_settings
        }
    settings = data
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
    return True

@eel.expose
def get_time_commands():
    return phrases.time_com
@eel.expose
def get_date_commands():
    return phrases.data_com
@eel.expose
def get_music_on_commands():
    return phrases.music_on_com
@eel.expose
def get_music_off_commands():
    return phrases.music_off_com
@eel.expose
def get_music_other_commands():
    return phrases.music_other_com
@eel.expose
def get_music_that_commands():
    return phrases.music_on_that_com
@eel.expose
def get_game_commands():
    return phrases.game_com
@eel.expose
def get_search_commands():
    return phrases.search_com
@eel.expose
def get_site_open_commands():
    return phrases.site_open_com
@eel.expose
def get_game_list():
    return mainSystem.gamesList
@eel.expose
def get_music_list():
    return mainSystem.musicList
@eel.expose
def process_text(text: str):
    text = TextCorect(text)
    text_list = (text[0]).split()
    if text[0] in phrases.time_com and text[1] >= 80:
        Time()
    elif text[0] in phrases.data_com and text[1] >= 80:
        Data()
    elif text[0] in phrases.music_on_com and text[1] >= 80:
        Music_phrases()
    elif text_list[0] in phrases.music_on_that_com and text[1] == -1:
        Music_phrases(str(text_list[1:]))
    elif text[0] in phrases.music_other_com and text[1] >= 80:
        mainSystem.Music_other()
    elif text[0] in phrases.music_off_com and text[1] == 0:
        mainSystem.Music_stop()
    elif text_list[0] in phrases.game_com and text[1] == -1:
        mainSystem.Game_start(str(text_list[1:]))
    elif text_list[0] in phrases.search_com and text[1] == -1:
        Search(str(text_list[1:]))
    elif text_list[0] in phrases.site_open_com and text[1] == -1:
        mainSystem.OpenSite(str(text_list[1:]))
    else:
        Talk(text)

eel.init('../GLADOSVoiceAssistant/GUI')
eel.start('index.html', mode='chrome', size=(600, 600))
