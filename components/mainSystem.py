import webbrowser
import pygame
from random import choice
import os
from pathlib import Path
from fuzzywuzzy import fuzz, process

current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
musicList = list(os.listdir(f"{parent_dir}/addContent/music"))
gamesList = list(os.listdir(f"{parent_dir}/addContent/games"))
 
def Random_answer():
    rate = [True, False, True, False]
    return choice(rate)

def Music_play(name_song):
    music = ""
    if name_song != "":
        music_check = list(process.extractOne(f"{name_song}.mp3", musicList, scorer=fuzz.token_sort_ratio))
        if music_check[1] >= 90:
            music = str(music_check[0])
    else:
        music = choice(musicList)
    pygame.mixer.init()
    pygame.mixer.music.load(f"{parent_dir}/addContent/music/{music}")
    pygame.mixer.music.play()
def Music_other():
    pygame.mixer.music.stop()
    music = choice(musicList)
    pygame.mixer.init()
    pygame.mixer.music.load(f"{parent_dir}/addContent/music/{music}")
    pygame.mixer.music.play()
def Music_stop():
    pygame.mixer.music.stop()

def Game_start(text):
    game = list(process.extractOne(text, gamesList, scorer=fuzz.token_sort_ratio))
    os.startfile(f"{parent_dir}/addContent/games/{game[0]}")

def OpenSite(text):
    fileSite = open(f"{parent_dir}/addContent/sites.txt", encoding="utf-8")
    text = text.replace("[", "").replace(",", "").replace("]", "").replace(":", "").replace("'", "")
    for i in fileSite:
        arr = list(map(str, i.split()))
        correct_text = list(process.extractOne(text, arr, scorer=fuzz.token_sort_ratio))
        for j in range(len(arr) - 1):
            if arr[j].replace("[", "").replace(",", "").replace("]", "").replace(":", "") == str(correct_text[0]).replace("[", "").replace(",", "").replace("]", "").replace(":", "").replace("'", "") and correct_text[1] >= 80:
                webbrowser.open(arr[-1])
                break