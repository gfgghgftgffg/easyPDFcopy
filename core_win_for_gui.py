import os, sys
# pyinstaller make sys.stdin/stdout NoneType, see https://stackoverflow.com/questions/17458728/when-is-sys-stdin-none-in-python
for _name in ('stdin', 'stdout', 'stderr'):
    if getattr(sys, _name) is None:
        setattr(sys, _name, open(os.devnull, 'r' if _name == 'stdin' else 'w'))
# set encoding to support 'gbk'
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

import keyboard, win32clipboard, pyperclip
import time
from colorama import init
init()


def get_clipboard():
    data = None
    # win32api deal with clipboard data type.
    win32clipboard.OpenClipboard()
    isStr = win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT)
    win32clipboard.CloseClipboard()
    # pyperclip deal with many encoding itself.
    if isStr:
        # data = win32clipboard.GetClipboardData()
        data = pyperclip.paste()
    return data

def set_clipboard(text):
    # win32clipboard.OpenClipboard()
    # win32clipboard.EmptyClipboard()
    # win32clipboard.SetClipboardText(text, win32clipboard.CF_TEXT)
    # win32clipboard.CloseClipboard()
    pyperclip.copy(text)


def changeClipboard():
    TEXT_ERR_LABEL = 'EASYPDFCOPY(E):'
    TEXT_UPDATE_LABEL = 'EASYPDFCOPY(*):'
    time.sleep(0.1)
    old_data = get_clipboard()

    outputdata = ''
    if old_data is None:
        outputdata = TEXT_ERR_LABEL + '\nTYPERTTNOT STR ERR\n'
    else:
        outputdata = TEXT_UPDATE_LABEL + old_data
        new_str = old_data.replace('\n',' ')
        new_str = new_str.replace('\r',' ')
        outputdata += TEXT_UPDATE_LABEL + "\n" + new_str
        set_clipboard(new_str)

    print(outputdata)


def run():
    keyboard.add_hotkey('ctrl+c', changeClipboard)
    while True:
        keyboard.wait()


run()
