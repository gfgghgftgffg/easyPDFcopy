import keyboard, pyperclip
import time
from colorama import Fore, init

init(autoreset=True)
def setClipboard():
    time.sleep(0.1)
    old_str = pyperclip.paste()
    print(Fore.YELLOW + old_str)
    new_str = old_str.replace('\n',' ')
    new_str = new_str.replace('\r',' ')
    print(' ')
    print(Fore.GREEN + new_str)
    print('----------------------')
    pyperclip.copy(new_str)

def run():
    keyboard.add_hotkey('ctrl+c', setClipboard)
    while True:
        keyboard.wait()


run()
