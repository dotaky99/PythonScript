import pyautogui
import time
import keyboard

num = int(input("방 인원수 만큼 입력하세요 : ")) - 1

while True:
    if keyboard.is_pressed('F5'):
        print("pressed")
        break

cnt = 0
while True:
    time.sleep(0.01)
    cnt = cnt + 1
    pyautogui.write('@')
    time.sleep(0.01)
    pyautogui.press('down',presses=cnt)
    time.sleep(0.3)
    pyautogui.press('enter')

    if cnt % 15 == 0:
        pyautogui.press('enter')

    if cnt == num:
        pyautogui.press('enter')
        break
