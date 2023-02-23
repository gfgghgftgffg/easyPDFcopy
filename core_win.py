import keyboard, win32clipboard
import time
from colorama import Fore, init
init(autoreset=True)



def get_clipboard():
    win32clipboard.OpenClipboard()
    data = None
    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
        data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def set_clipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_TEXT)
    win32clipboard.CloseClipboard()


def changeClipboard():
    time.sleep(0.1)
    old_data = get_clipboard()
    if old_data is None:
        print('NOT STR ERR')
    else:
        print(Fore.YELLOW + old_data)
        new_str = old_data.replace('\n',' ')
        new_str = new_str.replace('\r',' ')
        print(' ')
        print(Fore.GREEN + new_str)
        set_clipboard(new_str)

    print('----------------------')

def run():
    keyboard.add_hotkey('ctrl+c', changeClipboard)
    while True:
        keyboard.wait()


run()
