import os
import shutil
from time import sleep
from adb import screencap, get_devices


def start():
    screencap()
    sleep(3)


def loop():
    print('loop')
    exit()


def exit():
    raise ''


def onExit():
    dirs = os.listdir()
    for i in dirs:
        if not '.py' in i:
            shutil.rmtree(i)
    print('onExit')


if __name__ == "__main__":
    start()
    try:
        while True:
            loop()
            sleep(0.02)
    except:
        onExit()
