import os
from time import sleep
from subprocess import check_output, Popen, STDOUT


class KEYCODE:
    UNKNOWN = 0
    MENU = 1
    SOFT_RIGHT = 2
    HOME = 3
    BACK = 4
    CALL = 5
    ENDCALL = 6
    _0 = 7
    _1 = 8
    _2 = 9
    _3 = 10
    _4 = 11
    _5 = 12
    _6 = 13
    _7 = 14
    _8 = 15
    _9 = 16
    STAR = 17
    POUND = 18
    DPAD_UP = 19
    DPAD_DOWN = 20
    DPAD_LEFT = 21
    DPAD_RIGHT = 22
    DPAD_CENTER = 23
    VOLUME_UP = 24
    VOLUME_DOWN = 25
    POWER = 26
    CAMERA = 27
    CLEAR = 28
    A = 29
    B = 30
    C = 31
    D = 32
    E = 33
    F = 34
    G = 35
    H = 36
    I = 37
    J = 38
    K = 39
    L = 40
    M = 41
    N = 42
    O = 43
    P = 44
    Q = 45
    R = 46
    S = 47
    T = 48
    U = 49
    V = 50
    W = 51
    X = 52
    Y = 53
    Z = 54
    COMMA = 55
    PERIOD = 56
    ALT_LEFT = 57
    ALT_RIGHT = 58
    SHIFT_LEFT = 59
    SHIFT_RIGHT = 60
    TAB = 61
    SPACE = 62
    SYM = 63
    EXPLORER = 64
    ENVELOPE = 65
    ENTER = 66
    DEL = 67
    GRAVE = 68
    MINUS = 69
    EQUALS = 70
    LEFT_BRACKET = 71
    RIGHT_BRACKET = 72
    BACKSLASH = 73
    SEMICOLON = 74
    APOSTROPHE = 75
    SLASH = 76
    AT = 77
    NUM = 78
    HEADSETHOOK = 79
    FOCUS = 80
    PLUS = 81
    MENU = 82
    NOTIFICATION = 83
    SEARCH = 84
    _KEYCODE = 85


class PACKAGE_NAME:
    whatsapp = 'com.whatsapp'
    instagram = 'com.instagram.android'
    chrome = 'com.android.chrome'
    settings = 'com.android.settings'
    youtube = 'com.google.android.youtube'
    contacts = 'com.samsung.android.contacts'
    messages = 'com.samsung.android.messaging'
    twitter = 'com.twitter.android'
    skype = 'com.skype.raider'
    my_files = 'com.sec.android.app.myfiles'
    telegramx = 'org.thunderdog.challegram'
    vpn_phoenix = 'classicstudio.phoenix.proxy.vpn'


def get_devices():
    devices = str(check_output('adb devices')).replace('\\r\\n', ',').replace(
        '\\tdevice', '').replace('b\'', '').replace(',,', '')
    devices = devices.split(',')
    devices.pop(0)
    if len(devices) < 1:
        return list()
    devices[len(devices) - 1] = devices[len(devices) - 1][:-1]
    return devices


def screencap(device=None, wait=True, file_name='screencap.png'):
    if device is None:
        devices = get_devices()
        if len(devices) < 1:
            print('adb => No attached device was found.')
            return None
        device = devices[0]
    while not os.path.isdir(device):
        os.makedirs(device)
    process = Popen('adb -s '+str(device) + ' exec-out screencap -p > screencap.png' +
                    str(file_name), shell=True, cwd=os.getcwd() + '\\'+str(device)+'\\')
    if wait:
        process.wait()
    else:
        sleep(0.05)
    return str(os.getcwd()+'\\'+str(device)+'\\'+str(file_name))


def shell_exec(command, device=None, wait=True):
    if device is None:
        devices = get_devices()
        if len(devices) < 1:
            print('adb => No attached device was found.')
            return None
        device = devices[0]
    if not os.path.isdir(device):
        os.makedirs(device)
    with open(os.devnull, 'w') as fp:
        process = Popen('adb -s '+str(device) + ' shell ' + str(command),
                        shell=True, cwd=os.getcwd() + '\\'+str(device)+'\\', stdout=fp, stderr=STDOUT)
    if wait:
        process.wait()
    else:
        sleep(0.05)


def start_app(package, device=None, wait=True):
    shell_exec('monkey -p '+str(package) +
               ' -c android.intent.category.LAUNCHER 1')


def input_text(text, device=None, wait=True):
    shell_exec('input text "'+str(text)+'"', device=device, wait=wait)


def input_send_key(keycode, device=None, wait=True):
    try:
        keycode = int(keycode)
    except:
        print('adb input send key => invalid keycode')
        return
    shell_exec('input keyevent '+str(keycode), device=device, wait=wait)


def input_tap(pos, device=None, wait=True):
    if len(pos) != 2:
        print('adb input tap => position is not valid.('+str(pos)+')')
    try:
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
    except:
        print('adb input tap => position is not valid.(' + str(pos) + ')')
    shell_exec('input tap '+str(pos[0])+' ' +
               str(pos[1]), device=device, wait=wait)


def input_swipe(pos1, pos2, device=None, wait=True):
    if len(pos1) != 2:
        print('adb input swipe => position (1) is not valid.('+str(pos1)+')')
    try:
        pos1[0] = int(pos1[0])
        pos1[1] = int(pos1[1])
    except:
        print('adb input swipe => position (1) is not valid.(' + str(pos1) + ')')
    if len(pos2) != 2:
        print('adb input swipe => position (2) is not valid.('+str(pos2)+')')
    try:
        pos2[0] = int(pos2[0])
        pos2[1] = int(pos2[1])
    except:
        print('adb input swipe => position (2) is not valid.(' + str(pos2) + ')')
    shell_exec('input swipe '+str(pos1[0])+' ' + str(pos1[1]) + ' ' + str(
        pos2[0]) + ' ' + str(pos2[1]), device=device, wait=wait)


def input_draganddrop(pos1, pos2, device=None, wait=True):
    if len(pos1) != 2:
        print('adb input draganddrop => position (1) is not valid.('+str(pos1)+')')
    try:
        pos1[0] = int(pos1[0])
        pos1[1] = int(pos1[1])
    except:
        print('adb input draganddrop => position (1) is not valid.(' + str(pos1) + ')')
    if len(pos2) != 2:
        print('adb input draganddrop => position (2) is not valid.('+str(pos2)+')')
    try:
        pos2[0] = int(pos2[0])
        pos2[1] = int(pos2[1])
    except:
        print('adb input draganddrop => position (2) is not valid.(' + str(pos2) + ')')
    shell_exec('input draganddrop '+str(pos1[0])+' ' + str(pos1[1]) + ' ' + str(
        pos2[0]) + ' ' + str(pos2[1]), device=device, wait=wait)


def input_press(device=None, wait=True):
    shell_exec('input press', device=device, wait=wait)


def input_roll(deltapos, device=None, wait=True):
    if len(deltapos) != 2:
        print('adb input tap => position is not valid.('+str(deltapos)+')')
    try:
        deltapos[0] = int(deltapos[0])
        deltapos[1] = int(deltapos[1])
    except:
        print('adb input tap => position is not valid.(' + str(deltapos) + ')')
    shell_exec('input roll '+str(deltapos[0])+' ' +
               str(deltapos[1]), device=device, wait=wait)
