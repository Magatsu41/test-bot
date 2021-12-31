# -*- coding: utf-8 -*-

"""
Created on Tue Nov 17:12:11 2020

@author: Magatsu
"""

import keyboard, sys, pyautogui, time

pose_turn = 0

def fight():
    print("begin turn")
    sacrifice()
    if pose_turn==0:
        cast()
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

def stop_prgm():
    sys.exit("exiting...")

keyboard.add_hotkey("ctrl+e", fight)

keyboard.add_hotkey("ctrl+a", stop_prgm)

input()