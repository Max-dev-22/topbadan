import os
import shutil
from time import sleep
import adb


def start():
    adb.input_send_key(adb.KEYCODE.POWER, wait=False)


def loop():
    print('loop')
    exit()


def exit():
    raise ''


def onExit():
    dirs = os.listdir()
    for i in dirs:
        if not '.py' in i:
            while True:
                try:
                    shutil.rmtree(i)
                    break
                except:
                    pass
    print('onExit')


if __name__ == "__main__":
    start()
    try:
        while True:
            loop()
            sleep(0.02)
    except:
        onExit()
