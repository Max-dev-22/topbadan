import os
import shutil
from adb import *
from sys import argv
from time import sleep


def start():
    input_send_key(KEYCODE.POWER)
    sleep(10)


def loop():
    print('loop')
    exit()


def exit():
    raise ''


def onExit():
    dirs = os.listdir()
    devices = get_devices()
    for i in dirs:
        if i == '__pycache__' or i in devices:
            while True:
                try:
                    shutil.rmtree(i)
                    break
                except:
                    pass
    print('onExit')


def onBoot():
    sleep(0.1)


if __name__ == "__main__":
    argv.pop(0)
    while len(argv) > 0:
        if argv[0] == 'start':
            start()
            try:
                while True:
                    loop()
                    sleep(0.02)
            except:
                onExit()
        elif argv[0] == 'onboot':
            onBoot()
        else:
            print('Error: There is no argument named <'+str(argv[0])+'>')
        argv.pop(0)
    sleep(1)
