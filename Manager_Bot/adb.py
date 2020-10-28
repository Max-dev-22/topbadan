from subprocess import check_output


def get_devices():
    devices = str(check_output('adb devices')).replace('\\r\\n', ',').replace(
        '\\tdevice', '').replace('b\'', '').replace(',,', '')
    devices = devices.split(',')
    devices.pop(0)
    devices[len(devices)-1] = devices[len(devices)-1][:-1]
    return devices
