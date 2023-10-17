from Tkinter import *
from time import sleep
import ctypes

def opencd():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    
def closecd():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)

def textMenu():
    print('Что делать?')
    print('0. Закрыть и заниматься английским')
    print('1. Открыть дисковод')
    print('2. Закрыть дисковод')

    while True:
        todo = int(input('Делайте выбор: '))
        if(todo == 1):
            opencd()
        elif(todo == 2):
            closecd()
        else:
            print('Ой, ну и не надо')
            exit()

def buttonsMenu():
    root = Tk()
    root.title('CD Drive opener')
    root.configure(bg='gray')

    open_button = Button(root, text="Open", height= 3, width=20, command=opencd)
    open_button.pack()
    close_button = Button(root, text="Close", height= 3, width=20, command=closecd)
    close_button.pack()
    fun_button = Button(root, text="FUN", height= 4, width=25, bg='#54FA9B', command=makeFun)
    fun_button.pack()
    exit_button = Button(root, text="Exit", height= 2, width=15, command=exit)
    exit_button.pack()

    root.mainloop()

def makeFun():
    while True:
        opencd()
        sleep(2)
        closecd()
        sleep(2)

buttonsMenu()
    
