import ctypes
def opencd():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    
def closecd():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)

print('��� ������?')
print('0. ������� � ���������� ����������')
print('1. ������� ��������')
print('2. ������� ��������')

while True:
    todo = int(input('������� �����: '))
    if(todo == 1):
        opencd()
    elif(todo == 2):
        closecd()
    else:
        print('��, �� � �� ����')
        exit()
    
    
