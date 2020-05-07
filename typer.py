#!/usr/bin/python3

from pynput.keyboard import Key, Controller
from time import sleep
import random

keyboard = Controller()

while True:
    temp = random.randrange(1,9,2)
    temp2 = random.randrange(1,9,2)
    sleep(1)
    keyboard.press('a')
    keyboard.release('a')
    sleep(temp)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    sleep(temp2)
