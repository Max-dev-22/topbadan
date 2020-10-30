import os
import shutil
from sys import argv
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
        if not '.py' in i and i != 'assets' and i != 'heroku':
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
        print('Error: There is no argument named ' + str(argv[0]))
    sleep(1)
