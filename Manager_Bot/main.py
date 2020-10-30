import os
import shutil
from time import sleep


def start():
    sleep(1)


def loop():
    print('loop')
    exit()


def exit():
    raise ''


def onExit():
    dirs = os.listdir()
    for i in dirs:
        if not '.py' in i and i != 'assets':
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
