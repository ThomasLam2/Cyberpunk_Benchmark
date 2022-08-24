import os
import subprocess
import time
import pyautogui
import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

def pressdown(times): #Press Down function
    time.sleep(0.5)
    for i in range(times):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        time.sleep(0.2)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        time.sleep(0.2)
        #print("pressed down")

def pressrightshoulder(times): #Press right shoulder
    time.sleep(0.5)
    for i in range(times):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        gamepad.update()
        time.sleep(0.2)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        gamepad.update()
        time.sleep(0.2)
        #print("pressed down")

def pressa(): #Press a
    time.sleep(0.5)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
   #print("pressed a")

def pressb(): #Press b
    time.sleep(0.5)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    #print("pressed b")

def pressx(): #Press x
    time.sleep(0.5)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    #print("pressed x")

def pressstart(): #Press start
    time.sleep(1)
    gamepad.press_button(button=vg.XUSB_BUTTON(0x0010))
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON(0x0010))
    gamepad.update()
    #print("pressed start")
