import pyautogui

val = int(input())
for i in range(val+1):
    pyautogui.typewrite("#" * i)   
    pyautogui.press("enter")

