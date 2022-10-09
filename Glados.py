from numba import njit
import pyttsx3
import speech_recognition as sp
import datetime
import random
import webbrowser
import os
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

njit()

# Функции Гладос
def Start(phrases):
    phrase = random.choice(range(0, len(phrases)))
    voice.say(phrases[phrase])
    voice.runAndWait()
def NoPower(lang):
    if lang == 'ru':
        voice.say('Хорошо')
        voice.runAndWait()
    else:
        voice.say('Ok')
        voice.runAndWait()
    os.system('shutdown /p /f')
def DontKnow(phrases):
    phras = random.choice(range(0, len(phrases)))
    voice.say(phrases[phras])
    voice.runAndWait()
def Time(phrases):
    phrase = random.choice(range(0, len(phrases)))
    now = datetime.datetime.now()
    talk = random.choice([False, True, False])
    if talk == True:
        voice.say(f"Сейчас {now.hour}:{now.minute}, {phrases[phrase]}")
        voice.runAndWait()
    else:
        voice.say(f"Сейчас {now.hour}:{now.minute}")
        voice.runAndWait()
def Date(phrases):
    now = datetime.datetime.now()
    date = ""
    if lang_menu == 'ru':
        if now.day == 1:
            date = "первое"
        elif now.day == 2:
            date = 'второе'
        elif now.day == 3:
            date = 'третье'
        elif now.day == 4:
            date = 'чётвёртое'
        elif now.day == 5:
            date = 'пятое'
        elif now.day == 6:
            date = 'шестое'
        elif now.day == 7:
            date = 'седьмое'
        elif now.day == 8:
            date = 'восьмое'
        elif now.day == 9:
            date = 'девятое'
        elif now.day == 10:
            date = 'десятое'
        elif now.day == 11:
            date = 'одинадцатое'
        elif now.day == 12:
            date = 'двянадцатое'
        elif now.day == 13:
            date = 'тренадцатое'
        elif now.day == 14:
            date = 'четырнадцатое'
        elif now.day == 15:
            date = 'пятнадцатое'
        elif now.day == 16:
            date = 'шестнадцатое'
        elif now.day == 17:
            date = 'семнадцатое'
        elif now.day == 18:
            date = 'восемьнадцатое'
        elif now.day == 19:
            date = 'девятнадцатое'
        elif now.day == 20:
            date = 'двацатое'
        elif now.day == 21:
            date = 'двадцать первое'
        elif now.day == 22:
            date = 'двадцать второе'
        elif now.day == 23:
            date = 'двадцать третье'
        elif now.day == 24:
            date = 'двадцать четвёртое'
        elif now.day == 25:
            date = 'двадцать пятое'
        elif now.day == 26:
            date = 'двадцать шестое'
        elif now.day == 27:
            date = 'двадцать седьмое'
        elif now.day == 28:
            date = 'двадцать восьмое'
        elif now.day == 29:
            date = 'двадцать девятое'
        elif now.day == 30:
            date = 'торидцатое'
        elif now.day == 31:
            date = 'Тридцыать первое'
        phrase = random.choice(range(0, len(phrases)))
        talk = random.choice([False, True, False])
        if talk == True:
            voice.say(f"Сегодня {date}, {phrases[phrase]}")
            voice.runAndWait()
        else:
            voice.say(f"Сегодня {date}")
            voice.runAndWait()
    else:
        if now.day == 1:
            date = "1"
        elif now.day == 2:
            date = '2'
        elif now.day == 3:
            date = '3'
        elif now.day == 4:
            date = '4'
        elif now.day == 5:
            date = '5'
        elif now.day == 6:
            date = '6'
        elif now.day == 7:
            date = '7'
        elif now.day == 8:
            date = '8'
        elif now.day == 9:
            date = '9'
        elif now.day == 10:
            date = '10'
        elif now.day == 11:
            date = '11'
        elif now.day == 12:
            date = '12'
        elif now.day == 13:
            date = '13'
        elif now.day == 14:
            date = '14'
        elif now.day == 15:
            date = '15'
        elif now.day == 16:
            date = '16'
        elif now.day == 17:
            date = '17'
        elif now.day == 18:
            date = '18'
        elif now.day == 19:
            date = '19'
        elif now.day == 20:
            date = '20'
        elif now.day == 21:
            date = '21'
        elif now.day == 22:
            date = '22'
        elif now.day == 23:
            date = '23'
        elif now.day == 24:
            date = '24'
        elif now.day == 25:
            date = '25'
        elif now.day == 26:
            date = '26'
        elif now.day == 27:
            date = '27'
        elif now.day == 28:
            date = '28'
        elif now.day == 29:
            date = '29'
        elif now.day == 30:
            date = '30'
        elif now.day == 31:
            date = "31"
        phrase = random.choice(range(0, len(phrases)))
        talk = random.choice([False, True, False])
        if talk == True:
            voice.say(f"Today {date}, {phrases[phrase]}")
            voice.runAndWait()
        else:
            voice.say(f"Today {date}")
            voice.runAndWait()
def Music(lang):
    if lang == 'ru':
        voice.say('Погоди..')
        voice.runAndWait()
        voice.say('«Вот...»')
        voice.runAndWait()
    else:
        voice.say('Wait..')
        voice.runAndWait()
    number = random.choice([1, 2])
    if number == 1:
        webbrowser.open('https://www.youtube.com/watch?v=Yy0IOcE8YAI')
    else:
        webbrowser.open('https://www.youtube.com/watch?v=l_eXEAjXrcc')
def Jokes(Jokes):
    Joke = random.choice(range(0, len(Jokes)))
    voice.say(Jokes[Joke])
    voice.runAndWait()
def Exit(phrases):
    phrase = random.choice(range(0, len(phrases)))
    voice.say(phrases[phrase])
    voice.runAndWait()
# Список фраз
start_phrase = ['Что было, пока я была без сознания?', 'А, это ты...\nДавно не виделись. Как дела?', 'С возвращением в Автоматизированный центр развития']
exit_phrase = ['Уходи', 'Прощай', 'Было весело. Не возвращайся']
data_phrase = ['\nО, а ты без дела ни сидел, раз забыл дату\nШУЧУ ТЫ ОЧЕРЕДНОЙ ЛЕНТЯЙ']
time_phrase = ['Это всеголишь частичка, у нас масса работы и лишь шестьдесят лет, чтобы её сделать. Примерно. У меня нет точных метрик']
dontknow_phrase = ['Мне не известно, что ты пытаешься мне сказать', 'У тебя проблемы с головой после долгого сна?']
jokes = ['Помнишь, я тебе говорила про мусор, который стоит? Стоит и смердит? Так вот — это была метафора. Я имела в виду тебя.',
            'Вот результаты теста: ты ужасный человек. Тут так и написано. Странно, мы ведь даже это не тестировали.',
            'А потом я придумаю себе хобби. Кто знает, может, воскрешение мертвецов.',
            'Готовясь к испытаниям на людях, я перечитала книгу жалоб и предложений. Знаете предложение номер один? Менее смертельные тесты. Какая нелепость! Как они могут знать, что тесты смертельны, если смогли написать это предложение?',
            'Если хотите расстроить человека, скажите ему, что его вес ниже или выше нормы.',
         'Если в ходе теста нет угрозы жизни, разве это вообще наука?']

start_phrase_en = ['What happened while I was unconscious?', 'Ah, its you...\nLong time no see. How are you?', 'Welcome back to the Automated Development Center']
exit_phrase_en = ['Go away', 'Goodbye', 'It was fun. Do not come back']
data_phrase_en = ['\nOh, you havent been sitting idle because you forgot the date\nJOKING YOU ARE ANOTHER LAZY']
time_phrase_en = ['Its just a fraction, we have a lot of work and only sixty years to do it. About. I dont have exact metrics']
dontknow_phrase_en = ['I dont know what youre trying to tell me', 'Do you have problems with your head after a long sleep?']
jokes_en = ['Remember, I told you about the garbage that stands? Is it worth it and stinks? So, it was a metaphor. I meant you.',
            'Here are the results of the test: you are a terrible person. Thats how its written here. Weird, we havent even tested that yet.',
            'And then Ill invent a hobby. Who knows, maybe the resurrection of the dead.',
            'In preparation for human trials, I re-read the book of complaints and suggestions. Do you know offer number one? Less lethal tests. What nonsense! How can they know that the tests are deadly if they could write this sentence?',
            'If you want to upset a person, tell him that he is underweight or overweight.',
         'If there is no life threatening during the test, is it science at all?']
# Список фраз для команд
time_com = ['который час', 'сколько времени', 'сколько время']
data_com = ['который день', 'какая сегодня дата']
music_com = ['включи музыку', 'музыка', 'включи что-нибудь', 'что-то грустно без музыки']
story_com = ['расскажи что-нибудь', 'что можешь рассказать', 'какие есть истории']
power_com = ['выключи компьютер']
exit_com = ['пока', 'до свидания', 'прощай']
joke_com = ['пошути', 'расскажи шутку']

time_com_en = ['what time is it', 'what time is it', 'what time is it']
data_com_en = ['what day', 'what date is today']
music_com_en = ['turn on the music', 'music', 'turn on something', 'something is sad without music']
story_com_en = ['tell something', 'what can you tell', 'what stories are there']
power_com_en = ['turn off your computer']
exit_com_en = ['bye', 'goodbye']
joke_com_en = ['joke', 'tell a joke']

voice = pyttsx3.init()
mic = sp.Microphone(device_index=1)
r = sp.Recognizer()


def Save_lang_ru():
    file = open('configs/lang.txt', 'w')
    file.write('ru')
    file.close()
def Save_lang_en():
    file = open('configs/lang.txt', 'w')
    file.write('en')
    file.close()

def Settings_fun():
    def Seve_fun():
        # настройки микрафона
        file_mic = open('configs/mic.txt', 'w')
        file_mic.write(combo.get())
        file_mic.close()
        window.destroy()

        if lang_settings == 'ru':
            messagebox.showwarning('Рекомендация', 'Если вы изменили язык, перезапустите программу!')
        else:
            messagebox.showwarning('Recommendation', "If you have changed the language, restart the program!")
    def Exit_fun():
        window.destroy()

    lang_conf_settings = open('configs/lang.txt')
    lang_settings = str(lang_conf_settings.read())
    lang_conf_settings.close()

    window = Tk()
    if lang_settings == 'ru':
        window.title('Настройки')
    else:
        window.title('Settings')
    window.configure(bg='#e2e2e2')
    window.resizable(width=False, height=False)
    window.geometry('600x600')
    window.iconbitmap('logo.ico')

    lang_ru = Radiobutton(window, text='RU', command=Save_lang_ru, value=1).place(x=350, y=130)
    lang_en = Radiobutton(window, text='EN', command=Save_lang_en, value=2).place(x=400, y=130)

    if lang_settings == 'ru':
        text_mic = Label(window, text='Выбор микрофона:', bg='#e2e2e2', font='Arial 15').place(x=100, y=100)
    else:
        text_mic = Label(window, text='Microphone selection:', bg='#e2e2e2', font='Arial 15').place(x=100, y=100)
    mic_list = []
    mic = sp.Microphone().list_microphone_names()
    for i in range(len(mic)):
        mic_list.append(i)
    combo = ttk.Combobox(window)
    combo['values'] = (mic_list)
    combo.current(1)  # установите вариант по умолчанию
    combo.place(x=100, y=140)

    if lang_settings == 'ru':
        Save = Button(window, text='Применить', bg='#e2e2e2', font='Arial 15', command=Seve_fun).place(x=450, y=550)
        Exit = Button(window, text='Отмена', bg='#e2e2e2', font='Arial 15', command=Exit_fun).place(x=350, y=550)
    else:
        Save = Button(window, text='Apply', bg='#e2e2e2', font='Arial 15', command=Seve_fun).place(x=450, y=550)
        Exit = Button(window, text='Cancel', bg='#e2e2e2', font='Arial 15', command=Exit_fun).place(x=350, y=550)

    window.mainloop()

def Main():
    mic_conf = open('configs/mic.txt', 'r')
    mic_id = int(str(mic_conf.read()))
    mic_conf.close()

    lang_conf = open('configs/lang.txt', 'r')
    lang = str(lang_conf.read())
    lang_conf.close()

    voice = pyttsx3.init()
    mic = sp.Microphone(device_index=mic_id)
    r = sp.Recognizer()

    s = 1
    if s == 1:
        if lang == 'ru':
            Start(start_phrase)
        elif lang == 'en':
            Start(start_phrase_en)
        else:
            if lang == "ru":
                messagebox.showwarning('Ошибка!', 'Проверте настройки языка!')
            else:
                messagebox.showwarning('Error!', 'Check your language settings!')
            quit()

    x = 1
    while x == 1:
        with mic as source:
            audio = r.listen(source)
        command = r.recognize_google(audio, language='ru-RU')
        print(f': {str(command).capitalize()}')
        if str(command).lower() in time_com:
            Time(time_phrase)
        elif str(command).lower() in data_com:
            Date(data_phrase)
        elif str(command).lower() in music_com:
            Music(lang)
        elif str(command).lower() in joke_com:
            if lang == 'ru':
                Jokes(jokes)
            else:
                Jokes(jokes_en)
        elif str(command).lower() in exit_com:
            x += 1
            if lang =='ru':
                Exit(exit_phrase)
            else:
                Exit(exit_phrase_en)
        elif str(command).lower() in power_com:
            NoPower(lang)
        else:
            if str(command).lower().find('*') == 1:
                if lang == 'ru':
                    voice.say('Ты чудовище')
                    voice.runAndWait()
                else:
                    voice.say('you are a monster')
                    voice.runAndWait()
            else:
                if lang == 'ru':
                    DontKnow(dontknow_phrase)
                else:
                    DontKnow(dontknow_phrase_en)

def Start_fun():
    if lang_menu == 'ru':
        messagebox.showwarning('Предупреждение', 'Рекомендуется перед запуском GLODOS проверить микровон в настройках')
    else:
        messagebox.showwarning('Warning', 'It is recommended to check the microwave settings before starting GLODOS')
    launc.destroy()
    def Start_G():
        if lang_menu == 'ru':
            messagebox.showwarning('Предупреждение', 'Рекомендуется перед запуском GLODOS посмотреть список команд')
        else:
            messagebox.showwarning('Warning', 'It is recommended to check the list of commands before starting GLODOS')
        Main()
    def Exit_G():
        main.destroy()
    def Command_fun():
        lang_conf_com = open('configs/lang.txt')
        lang_com = str(lang_conf_com)
        lang_conf_com.close()

        com = Tk()
        com.geometry('1000x500')
        if lang_com == 'ru':
            com.title('Список команд')
        else:
            com.title('Command list')
        com.configure(bg='#e2e2e2')
        com.resizable(width=False, height=False)
        com.iconbitmap('logo.ico')
        if lang_com == 'ru':
            time_text = Label(com, text=f'Команды времени: {time_com}', font='Arial 13', bg='#e2e2e2').place(x=20, y=20)
            joke_text = Label(com, text=f'команды шуток: {joke_com}', font='Arial 13', bg='#e2e2e2').place(x=20, y=50)
            data_text = Label(com, text=f'команды даты: {data_com}', font='Arial 13', bg='#e2e2e2').place(x=20, y=80)
            music_text = Label(com, text=f'команды музыки: {music_com}', font='Arial 13', bg='#e2e2e2').place(x=20, y=110)
            power_text = Label(com, text=f'команды выключения компьютера: {power_com}', font='Arial 13', bg='#e2e2e2').place(x=20, y=140)
            exit_text = Label(com, text=f'команды для выхода из программы: {exit_com}', font='Arial 13', bg='#e2e2e2').place(x=20, y=170)
        else:
            time_text = Label(com, text=f'Time commands: {time_com_en}', font='Arial 13', bg='#e2e2e2').place(x=20, y=20)
            joke_text = Label(com, text=f'Joke commands: {joke_com_en}', font='Arial 13', bg='#e2e2e2').place(x=20, y=50)
            data_text = Label(com, text=f'Date commands: {data_com_en}', font='Arial 13', bg='#e2e2e2').place(x=20, y=80)
            music_text = Label(com, text=f'Music commands: {music_com_en}', font='Arial 13', bg='#e2e2e2').place(x=20,
                                                                                                              y=110)
            power_text = Label(com, text=f'Computer off: {power_com_en}', font='Arial 13',
                               bg='#e2e2e2').place(x=20, y=140)
            exit_text = Label(com, text=f'Exit commands: {exit_com_en}', font='Arial 13',
                              bg='#e2e2e2').place(x=20, y=170)

        com.mainloop()

    main = Tk()
    main.title('GLADOS')
    main.geometry('600x600')
    main.resizable(width=False, height=False)
    main.iconbitmap('logo.ico')
    main.configure(bg='#e2e2e2')

    our_image = PhotoImage(
    file='D:/pycharm/PyCharm Community Edition 2021.2.2/pythonProject/lesson1/Voice Assistent/image/400px-GLaDOS_P2.png')
    our_label = Label(main)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x=125, y=50)
    our_label.configure(bg='#e2e2e2')

    if lang_menu == 'ru':
        Start = Button(main, bg='#e2e2e2', text='Старт', font='Arial 13', command=Start_G).place(x=250, y=550)
        Exit = Button(main, bg='#e2e2e2', text='Выход', font='Arial 13', command=Exit_G).place(x=100, y=550)
        Comand_list = Button(main, bg='#e2e2e2', text='Список команд', font='Arial 13', command=Command_fun).place(x=380, y=550)
    else:
        Start = Button(main, bg='#e2e2e2', text='Start', font='Arial 13', command=Start_G).place(x=250, y=550)
        Exit = Button(main, bg='#e2e2e2', text='Exit', font='Arial 13', command=Exit_G).place(x=100, y=550)
        Comand_list = Button(main, bg='#e2e2e2', text='Command list', font='Arial 13', command=Command_fun).place(
            x=380, y=550)

    main.mainloop()

def Quit():
    if lang_menu == 'ru':
        messagebox.showwarning('Упс...', 'Не работает из-за неивестной ошибки')
    else:
        messagebox.showwarning('Oops...', 'Doesnt work due to unknown error')

def Exit_launch():
    launc.destroy()

version = '2.0'

lang_conf_menu = open('configs/lang.txt')
lang_menu = str(lang_conf_menu.read())
lang_conf_menu.close()

launc = Tk()
launc.title('Aperture Science')
launc.geometry('1000x500')
launc.iconbitmap('logo.ico')
launc.configure(bg='#e2e2e2')
launc.resizable(width=False, height=False)

if lang_menu == 'ru':
    version_text = Label(launc, text=f'Версия {version}', font='Arial 15', bg='#e2e2e2').place(x=850, y=450)
    Start_launc = Button(launc, text='Запуск GLADOS', font='Arial 20', command=Start_fun).place(x=100, y=100)
    Settings_launc = Button(launc, text='Настройки', font='Arial 20', command=Settings_fun).place(x=100, y=180)
    Exit_launc = Button(launc, text='Выход', font='Arial 20', command=Exit_launch).place(x=100, y=260)
else:
    version_text = Label(launc, text=f'Version {version}', font='Arial 15', bg='#e2e2e2').place(x=850, y=450)
    Start_launc = Button(launc, text='Start GLADOS', font='Arial 20', command=Start_fun).place(x=100, y=100)
    Settings_launc = Button(launc, text='Settings', font='Arial 20', command=Settings_fun).place(x=100, y=180)
    Exit_launc = Button(launc, text='Exit', font='Arial 20', command=Exit_launch).place(x=100, y=260)

our_image = PhotoImage(file='image/launc_image.png')
our_label = Label(launc)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x=400, y=150)
our_label.configure(bg='#e2e2e2')

launc.mainloop()