# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:15:11 2020

@author: Magatsu
"""

import pyautogui
import time
import sys
import os
import keyboard

metier = 0
job_tab = ["none", "alchemist"]
job_mats = []
wait_collect = 0.0
mats_number = 0
need_to_stop = 0

def launch_bot():
    print("Start to collect mats on current map for job "+job_tab[metier])
    time.sleep(5)
    make_collect()

def check_if_battle():
    try:
        imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/skip.png", confidence=0.9)
        x, y = imageToParse
        input()
        sys.exit("You are in battle, stopping bot")
    except:
        print("Not in battle, searching for mats")
        return

def job_mat_list(job):
    global job_mats
    if job==1:
        job_mats = ["none", "lin", "chanvre", "trefle"]

def make_collect():
    global mats_number
    global need_to_stop
    check_if_battle()
    mats_number = sum(os.path.isdir(os.path.join("./img/"+job_tab[metier], i)) for i in os.listdir("./img/"+job_tab[metier]))
    j = 1
    while j<=mats_number:
        need_to_stop = 0
        path, dirs, files = next(os.walk("./img/"+job_tab[metier]+"/"+str(j)))
        file_count = len(files)
        print(str(file_count)+" images found for current mats")
        search_img_to_collect(file_count, j)
        time.sleep(.3)
        if need_to_stop==0:
            search_collect_button()
        j = j+1
    make_collect()

def search_img_to_collect(counter, curmat):
    print("Loocking for "+job_mats[curmat])
    global need_to_stop
    i = 1
    while i<=counter:
        try:
            print("Loop "+str(i))
            path_to_mats = "./img/"+job_tab[metier]+"/"+str(curmat)+"/"+str(i)+".png"
            imageToParse  = pyautogui.locateCenterOnScreen(path_to_mats, grayscale=True, confidence=0.8)
            x, y = imageToParse
            print("Mats found at X="+str(x)+" and Y="+str(y))
            print("clicking at following coordinates")
            pyautogui.click(x, y)
            return
        except:
            i=i+1
    print("No mats could be found for current value")
    need_to_stop = 1

def search_collect_button():
    path_to_collect = "./img/"+job_tab[metier]+"/collect.png"
    try:
        imageToParse  = pyautogui.locateCenterOnScreen(path_to_collect, grayscale=True, confidence=0.8)
        x, y = imageToParse
        print("Collect button found at X="+str(x)+" and Y="+str(y))
        print("clicking at following coordinates")
        pyautogui.click(x, y)
        time.sleep(.3)
        pyautogui.moveTo(100, 100)
        time.sleep(wait_collect)
        return
    except:
        print("Collect button could not be found, retrying...")
        return

def stop_prgm():
    sys.exit("exiting...")

keyboard.add_hotkey("ctrl+a", stop_prgm)

print("Starting Magatsu's collect bot v0.1a")
print(" ")
print("Select the desired job...")
print("(hint :")
print("Alchemist : 1")
print("Other job will be added later)")
print(" ")

metier = input()
metier = int(metier)

if isinstance(metier, int):
    if metier+1>len(job_tab):
        print("Your choise is not on the list")
        sys.exit("exiting...")
    elif metier==0:
        print("Your choise is not on the list")
        sys.exit("exiting...")
    else :
        print("You chose the job: "+job_tab[metier])
        wait_collect = float(input("Enter the waiting time in second between collect (ex : 2.5) : "))
        print(str(wait_collect)+" seconds will elapse between each collect")
        job_mat_list(metier)
        launch_bot()
else :
    print("Please type an integer")
    sys.exit("exiting...")