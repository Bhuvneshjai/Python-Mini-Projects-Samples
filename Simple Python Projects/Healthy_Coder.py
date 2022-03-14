# Healthy Coder
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 1 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 2 min
# Physical Activity - physical.mp3 - every 3 min - ExDone
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    init_water = time()
    init_eyes = time()
    init_excercise = time()
    watersecs = 1*60
    eyessecs = 2*60
    exsecs = 3*60
    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time - Enter 'Drank' to stop the alarm : ")
            musiconloop('water.mp3','Drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eyes Excercise Time - Enter 'DoneEyes' to stop the alarm : ")
            musiconloop("eyes.mp3",'DoneEyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_excercise > exsecs:
            print("Physical Activity Time - Enter 'DoneEx' to stop the alarm : ")
            musiconloop("physical.mp3",'DoneEx')
            init_excercise = time()
            log_now("Physical Activity done at")