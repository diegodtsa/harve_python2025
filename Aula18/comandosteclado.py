import pyautogui
import time

time.sleep(2)

pyautogui.hotkey("ctrl", "alt", "t")
time.sleep(2)
pyautogui.hotkey('alt', 'f10')


pyautogui.write("nano", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.write("Hello World", interval= 0.20)
pyautogui.hotkey("ctrl", "o")
time.sleep(2)

pyautogui.write("hello_world.txt", interval= 0.20)
pyautogui.press("ENTER")
pyautogui.hotkey("ctrl", "x")
time.sleep(2)

pyautogui.write("ls -l", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.write("rm hello_world.txt", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.write("ls -l", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.write("exit", interval= 0.20)
pyautogui.press("ENTER")



