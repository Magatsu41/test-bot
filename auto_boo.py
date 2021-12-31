# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:39:14 2020

@author: Magatsu
"""

import keyboard, sys, pyautogui, time, os

pose_turn = 0
mode = 0
success = False

def fight():
    print("begining turn actions")
    pyautogui.moveTo(100, 100)
    sacrifice()
    if pose_turn==0:
        pyautogui.moveTo(100, 100)
        cast()
        pyautogui.moveTo(100, 100)
    else:
        print("Skiping")
        try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/skip.png", confidence=0.9)
            x, y = imageToParse
            print("Skip found at X="+str(x)+" and Y="+str(y))
            pyautogui.click(x, y)
            time.sleep(.350)
            return
        except:
            print("image not found")
            return
    return
    
def sacrifice():
    global pose_turn
    try:
        imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/spell2.png", confidence=0.85)
        x, y = imageToParse
        print("Sacrifice available")
        pyautogui.click(x, y)
        pyautogui.moveTo(100, 100)
        time.sleep(.250)
    except:
        print("Sacrifice not available")
        pose_turn = 0
        return
    try:
        imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/me.png", confidence=0.9)
        x, y = imageToParse
        print("Self found at X="+str(x)+" and Y="+str(y))
        pyautogui.click(x, y)
        time.sleep(.350)
        return
    except:
        print("image not found")
        return

def cast():
        print("Attacking")
        try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/spell1.png", confidence=0.9)
            x, y = imageToParse
            print("Spell found at X="+str(x)+" and Y="+str(y))
            pyautogui.click(x, y)
            time.sleep(.250)
        except:
            print("image not found")
            return
        try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/me.png", confidence=0.9)
            x, y = imageToParse
            print("Self found at X="+str(x)+" and Y="+str(y))
            pyautogui.click(x, y)
            time.sleep(.350)
        except:
            print("image not found")
            return
        try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/skip.png", confidence=0.9)
            x, y = imageToParse
            print("Skip found at X="+str(x)+" and Y="+str(y))
            pyautogui.click(x, y)
            return
        except:
            print("image not found")
            return

def search_boo():
    global success
    path, dirs, files = next(os.walk("./img/fight/boo"))
    file_count = len(files)
    print("Loocking for boo")
    i = 1
    while i<=file_count:
        try:
            path_to_mats = "./img/fight/boo/"+str(i)+".png"
            imageToParse  = pyautogui.locateCenterOnScreen(path_to_mats, grayscale=True, confidence=0.7)
            x, y = imageToParse
            print("Boo found at X="+str(x)+" and Y="+str(y))
            print("clicking at following coordinates")
            pyautogui.click(x, y)
            success=True
            time.sleep(.500)
            return
        except:
            i=i+1
    print("No boo found")

def attack_target():
    global success
    try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/misc/attack.png", confidence=0.9)
            x, y = imageToParse
            pyautogui.click(x, y)
            success = True
            time.sleep(3.0)
            return
    except:
            print("attack image not found")
            return

def check_ready():
    global success
    global mode
    i = 0
    while i<3:
        try:
                imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/misc/ready.png", confidence=0.9)
                x, y = imageToParse
                pyautogui.click(x, y)
                success = True
                mode = 1
                print("Battle engaged")
                time.sleep(3.0)
                return
        except:
                print("ready button not found, checking again in 2s")
                i=i+1
                time.sleep(2.0)
    print("Combat seemingly not started, back to search mode")

def battle_actions():
    print("Checking if level up")
    global mode
    try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/misc/ok.png", confidence=0.9)
            x, y = imageToParse
            pyautogui.click(x, y)
            print("You level up")
            mode = 0
            time.sleep(1.0)
            check_over()
            return
    except:
            print("No level up")
            pyautogui.moveTo(100, 100)
            check_over()

def check_over():
    print("Checking if battle over")
    global mode
    try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/misc/end.png", confidence=0.9)
            x, y = imageToParse
            pyautogui.click(x, y)
            print("Battle's over")
            mode = 0
            time.sleep(1.0)
            return
    except:
            print("Battle not over, issuing combat actions")
            pyautogui.moveTo(100, 100)
            check_if_turn()

def check_if_turn():
    print("Checking if player's turn")
    try:
            imageToParse  = pyautogui.locateCenterOnScreen("./img/fight/misc/turn.png", confidence=0.9)
            x, y = imageToParse
            print("Player's turn")
            time.sleep(1.0)
            fight()
    except:
            print("Not your turn yet")
            return

def big_balls():
    print("Bot init")
    global mode
    global success
    success = False
    if mode==0:
        success = False
        pyautogui.moveTo(100, 100)
        search_boo()
        if success==True:
            success = False
            print("Attacking target")
            attack_target()
            if success==True:
                check_ready()
                success=False
                pyautogui.moveTo(100, 100)
                big_balls()
            else:
                pyautogui.moveTo(100, 100)
                big_balls()
        else:
            time.sleep(2.0)
            pyautogui.moveTo(100, 100)
            big_balls()
    elif mode==1:
        pyautogui.moveTo(100, 100)
        battle_actions()
        pyautogui.moveTo(100, 100)
        time.sleep(5.0)
        big_balls()

def stop_prgm():
    sys.exit("exiting...")
    input()

keyboard.add_hotkey("ctrl+a", stop_prgm)

big_balls()