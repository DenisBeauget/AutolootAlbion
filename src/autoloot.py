#! https://github.com/asweigart/pyautogui

import keyboard
import pyautogui
import sys



def loopPnj():
    pyautogui.click(x=208, y=846)
    pyautogui.moveTo(x=1591,y=553)
    

while True:
    if keyboard.read_key() == "ù":
        loopPnj()
    if keyboard.read_key() == "!":
        pyautogui.moveTo(x=121,y=867)
        pyautogui.click()
        pyautogui.moveTo(x=1591,y=553)


#! Pour récup les pos
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')







