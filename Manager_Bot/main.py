from time import sleep
from funcs import print_devices_list


def start():
    print_devices_list()


def loop():
    print('loop')
    exit()


def exit():
    raise ''


def onExit():
    print('onExit')


if __name__ == "__main__":
    start()
    try:
        while True:
            loop()
            sleep(0.02)
    except:
        onExit()
