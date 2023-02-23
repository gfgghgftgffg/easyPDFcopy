import os, subprocess, signal
import keyboard


PID = -1

def start():
    global PID
    if -1 == PID:
        P = subprocess.Popen(['python','core_win.py'])
        PID = P.pid
        print('Started, PID=',PID,'\n\n')
    else:
        print('One process has been started, PID=',PID,'\n\n')

def stop():
    global PID
    if -1 != PID:
        os.kill(PID, signal.SIGTERM)
        PID = -1
        print('Killed PID=',PID,'\n\n')
    else:
        print('No process is running.\n\n')


keyboard.add_hotkey('ctrl+f1', start)
keyboard.add_hotkey('ctrl+f2', stop)
start()
while True:
   keyboard.wait()