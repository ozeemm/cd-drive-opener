import ctypes
def opencd():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    
def closecd():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)

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
    
    
