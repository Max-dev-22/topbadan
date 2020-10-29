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


def screencap(device=None, file_name='screencap.png', wait=True):
    if device is None:
        devices = get_devices()
        if len(devices) < 1:
            print('No attached device was found.')
            return None
        device = devices[0]
    if not os.path.isdir(device):
        os.makedirs(device)
    process = Popen('adb -s '+str(device) +
                    ' exec-out screencap -p > screencap.png'+str(file_name), shell=True, cwd=os.getcwd()+'\\'+str(device)+'\\')
    if wait:
        process.wait()
    return str(os.getcwd()+'\\'+str(device)+'\\'+str(file_name))


def shell_exec(device, command):
    print('')
