import keyboard
import pyautogui
import time

keyboard.wait("a")
while True:
    pyautogui.moveTo(255, 580, duration=1)
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveTo(1185, 865, duration=1)
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.hotkey('browser-back')
    time.sleep(2)
    pyautogui.moveTo(255, 580, duration=1)
    pyautogui.scroll(-160)
