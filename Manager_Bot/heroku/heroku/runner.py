from os import path, getcwd
from subprocess import Popen


def Telegram(wait=True):
    process = Popen('python main.py', shell=True,
                    cwd=path.join(getcwd(), 'Telegram'))
    if wait:
        process.wait()
