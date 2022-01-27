# # Healthy Programmer
# # 9am - 5pm
# # water - water.mp3 - 3.5 ltr - Drank - log
# # Eyes - eyes.mp3 - every 30 min - eyDone - log
# # Physical Activity - physical.mp3 every - 45 min - log
# # Pygame module to play audio
#
# import time
# import pygame
#
# # music did not played hence i have printed it as well
#
# def playmusic(file):
#     print(file)
#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()
#
# def IsOfficeTime(currenttime):
#     if currenttime>'09:00:00' and currenttime<'17:00:00':
#         return True
#     else:
#         return False
#
# NumberofWaterRemaining = 18
#
# WaterAfterEvery = 1200 #seconds - 20 minutes
# EyeExcerciseAfterEvery = 1800 #seconds - 30 minutes
# PysicalExcerciseAfterEvery = 2700 #seconds - 45 minutes
#
# waterMp3 = 'water.mp3'
# eyesMp3 = 'eyes.mp3'
# PhysicalMp3 = 'physical.mp3'
#
# currenttime = time.strftime("%H:%M:%S")
# WaterTakenAt = time.time()
# EyeExcerciseAt = time.time()
# PhysicalExcerciseAt = time.time()
#
# SleepTime = 60 #sleep time in seconds it will check after every 60 seconds
#
# while(IsOfficeTime(currenttime)):
#     #check for water
#     if NumberofWaterRemaining>0:
#         if (time.time()-WaterTakenAt)>WaterAfterEvery:
#             #water after every 20 minutes
#             print("Time to Drink water")
#             while True:
#                 playmusic(waterMp3)
#                 if input("Enter Done if you had water:").lower()=="done":
#                     WaterTakenAt=time.time()
#                     NumberofWaterRemaining -=1
#                     break
#
#         if (time.time()-EyeExcerciseAt)>EyeExcerciseAfterEvery:
#             print("Time to do eye excercise")
#             while True:
#                 playmusic(eyesMp3)
#                 if input("Enter Done if you done eye excercise:").lower()=="done":
#                     EyeExcerciseAt=time.time()
#                     break
#
#         if (time.time()-PhysicalExcerciseAt)>PysicalExcerciseAfterEvery:
#             print("Time to do Physical Excercise")
#             while True:
#                 playmusic(PhysicalMp3)
#                 if input("Enter Done if you done physical excercise:").lower()=="done":
#                     PhysicalExcerciseAt==time.time()
#                     break
#
#     time.sleep(SleepTime)
#     currenttime = time.strftime("%H:%M:%S")













# water 200 ML in 25 min
# Eyes in 30 min
# Excercise in 45 min

import time
from pygame import mixer
p = time.localtime().tm_hour
# print(p)

def water():
    print("Please Drink 200 ML of water")
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    w=input("enter 'Drank' to stop the audio: ")
    if w == "Drank":
        mixer.music.stop()

def physical():
    print("Please do excercise")
    mixer.init()
    mixer.music.load("physical.mp3")
    mixer.music.play()
    p=input("enter 'Done' to stop the audio: ")
    if p=="Done":
        mixer.music.stop()

def eye():
    print("Please do eye care routine")
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play()
    e=input("enter 'Blink' to stop the audio: ")
    if e=="Blink":
        mixer.music.stop()

wtime=0000
etime=0000
ptime=0000

while (p>=9) and (p<=17):
    now = time.time()
    if now-wtime>25*60:
        water()
        wtime=time.time()
        with open("Water.txt","a") as file:
            file.write(time.asctime(time.localtime()))
    if now-etime>30*60:
        eye()
        etime=time.time()
        with open("Eyes.txt","a") as file:
            file.write(time.asctime(time.localtime()))
    if now-ptime>45*60:
        physical()
        ptime=time.time()
        with open("Pysical.txt","a") as file:
            file.write(time.asctime(time.localtime()))
    time.sleep(60)

if p<9:
    print("Your time will start at 9:00 AM  - 5:00 PM")
if p>17:
    print("You are done for the day! Program will start at 9:00 AM localtime Tomorrow")













#
# # 9am - 5pm
# # Water - water.mp3 (3.5 litres = 15 - 18 glasses) - Drank - log
# # Eyes - eyes.mp3 - every 30 min - EyDone - log
# # Physical activity - physical.mp3 every - 45 min - ExDone - log
# # Rules: Pygame module to play audio
#
# from pygame import mixer
# import datetime
# import time
#
#
# # Start and Stop time Configuration for a particular day
# current_time = datetime.datetime.now()
# dt_string = f"{current_time.day}/{current_time.month}/{current_time.year} 9:00:00"
# start = datetime.datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")  # Considering date is in dd/mm/yyyy format
# stop = start + datetime.timedelta(hours=8)  # 8 hrs working
#
# # Drink Water Configuration
# water_limit = 3500  # in ml
# glass_size = 200  # in ml
# no_of_glass = round(water_limit / glass_size)
# total_working_time = 8 * 60 * 60  # 8 hrs working (in seconds)
# water_interval = total_working_time / no_of_glass  # every 1600 seconds
#
#
# # Eye Exercise Configuration
# eyes_interval = 30 * 60  # Every 30 minutes (in seconds)
#
# # Physical Exercise Configuration
# physical_interval = 45 * 60  # Every 45 minutes(in seconds)
#
#
# def play_music(m):
#     mixer.init()  # Starting the mixer
#     mixer.music.load(m)  # Loading the tunes
#     mixer.music.set_volume(0.7)  # Setting the volume
#     mixer.music.play(-1)  # Start playing the song and continue repeating the piece of music
#
#
# def file_write(activity):
#     with open('health_report.txt', 'a+') as f:
#         data = '[' + str(datetime.datetime.now()) + ']  ' + activity
#         f.write(data + '\n')
#
#
# def water_reminder():
#     while True:
#         play_music('water.mp3')
#         flag_water = input("Drink Water. Enter 'drank' to stop the alarm:  \n ").upper()
#         if flag_water == 'DRANK':
#             mixer.music.stop()
#             file_write(flag_water)
#             break
#         else:
#             continue
#
#
# def eyes_reminder():
#     while True:
#         play_music('eyes.mp3')
#         flag_eyes = input("Do eyes exercise. Enter 'eydone' to stop the alarm:\n ").upper()
#         if flag_eyes == 'EYDONE':
#             mixer.music.stop()
#             file_write(flag_eyes)
#             break
#         else:
#             continue
#
#
# def physical_reminder():
#     while True:
#         play_music('physical.mp3')
#         flag_physical = input("Do physical activity. Enter 'exdone' to stop the alarm: \n ").upper()
#         if flag_physical == 'EXDONE':
#             mixer.music.stop()
#             file_write(flag_physical)
#             break
#         else:
#             continue
#
#
# while start < current_time < stop:
#     print(current_time)
#     if datetime.datetime.now() < stop - datetime.timedelta(seconds=water_interval):
#         time.sleep(water_interval)
#         water_reminder()
#     else:
#         break
#     if datetime.datetime.now() < stop - datetime.timedelta(seconds=200):
#         time.sleep(eyes_interval-water_interval)  # run after 200 sec of water reminder
#         eyes_reminder()
#     else:
#         break
#     if datetime.datetime.now() < stop - datetime.timedelta(minutes=15):
#         time.sleep(physical_interval-eyes_interval)  # run after 15 min of eye exercise
#         physical_reminder()
#     else:
#         break
#     current_time = datetime.datetime.now()
# else:
#     print("It is NOT office time, Take Rest !!!")













# import datetime
# from pygame import mixer
#
# while True:
#     t = datetime.datetime.today()
#     time = t.strftime('%H:%M:%S')
#     if time < "17:00:00" and time > "09:00:00":
#         break
#     print(type(time))
#     water_time = t + datetime.timedelta(seconds=10)
#     water_time = water_time.strftime('%H:%M:%S')
#
#     exercise_time = t + datetime.timedelta(seconds=30)
#     exercise_time = exercise_time.strftime('%H:%M:%S')
#
#     physical_time = t + datetime.timedelta(seconds=50)
#     physical_time = physical_time.strftime('%H:%M:%S')
#
#     while True:
#         time = datetime.datetime.strftime(datetime.datetime.today(), '%H:%M:%S')
#         if time == water_time:
#             print('drink water')
#             mixer.init()
#             mixer.music.load('song1.mp3')
#             mixer.music.play()
#             user_intput = input('Are you drunk water (y/n):')
#             if user_intput == 'y':
#                 with open('water.txt', 'a') as f:
#                     f.write(f'you drink water at{time}\n')
#                 mixer.music.stop()
#             else:
#                 print('thats sounds bad Idiot')
#                 mixer.music.stop()
#
#         elif time == exercise_time:
#             print('its eyes exercise time ')
#             mixer.init()
#             mixer.music.load('song1.mp3')
#             mixer.music.play()
#             user_intput = input('Are you done eye exercise (y/n):')
#             if user_intput == 'y':
#                 with open('eye.txt', 'a') as f:
#                     f.write(f'you done the eye exercise at {time}\n')
#                 mixer.music.stop()
#             else:
#                 print('thats sounds bad Idiot')
#                 mixer.music.stop()
#
#         elif time == physical_time:
#             print('its physical exercise time')
#             mixer.init()
#             mixer.music.load('song1.mp3')
#             mixer.music.play()
#             user_intput = input('Are you done pyshical work (y/n):')
#             if user_intput == 'y':
#                 with open('physical.txt', 'a') as f:
#                     f.write(f'you done physical work at {time}\n')
#                 mixer.music.stop()
#             else:
#                 print('thats sounds bad Idiot')
#                 mixer.music.stop()