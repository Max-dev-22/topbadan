import os
from subprocess import check_output, Popen


def get_devices():
    devices = str(check_output('adb devices')).replace('\\r\\n', ',').replace(
        '\\tdevice', '').replace('b\'', '').replace(',,', '')
    devices = devices.split(',')
    devices.pop(0)
    if len(devices) < 1:
        return list()
    devices[len(devices)-1] = devices[len(devices)-1][:-1]
    return devices


def screenshot(device, wait=True):
    if not os.path.isdir(device):
        os.makedirs(device)
    process = Popen('adb -s '+str(device) +
                    ' exec-out screencap -p > screencap.png', shell=True, cwd=os.getcwd()+'\\'+str(device)+'\\')
    if wait:
        process.wait()
