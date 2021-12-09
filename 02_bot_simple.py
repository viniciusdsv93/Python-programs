import pyautogui
from time import sleep

def write(*n):
    for i in n:
        pyautogui.write(i)
        sleep(0.01)

pyautogui.press('win')
sleep(1)
write('b','l','o','c','o',' ','d','e',' ','n','o','t','a','s')
pyautogui.press('backspace')
sleep(1)
pyautogui.press('enter')
sleep(1)
write('O','l','h','a',' ','c','o','m','o',' ',
'e','u',' ','s','o','u',' ','a','u','t','o','m','a','t','i','z','a','d','o',' ',':','D')
