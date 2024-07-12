from BirdBrain import Finch
import time 
import keyboard
from pynput.keyboard import Key, Listener


fin = Finch('A')

speed = int(input("What speed would you like to use? (Recommended: 1-10)")) #for customization (and so I can finally get my kids to understand input())
        
def on_press(key):
    try:
        if key.char == 'w':
            fin.setMotors(speed,speed)
        if key.char == 'a':
            fin.setMotors(-speed,speed)
        if key.char == 's':
            fin.setMotors(-speed,-speed)
        if key.char == 'd':
            fin.setMotors(speed,-speed)
        time.sleep(0.01)
    except AttributeError:
        pass

def on_release(key):
    try:
        if key == Key.esc:
            return False #quits tracking keyboard
        if key.char in ['w','a','s','d']:
            fin.setMotors(0,0)
    except AttributeError:
        pass

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()








