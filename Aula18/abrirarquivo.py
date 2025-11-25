import pyautogui
import time

time.sleep(2)


pyautogui.click(x=28,y=60, clicks= 1) 
time.sleep(3)
pyautogui.click(x=315,y= 98, clicks= 1) 
time.sleep(3)

pyautogui.write("cotacao dolar", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(3)

pyautogui.mouseDown(x=286, y=348)
time.sleep(2)
pyautogui.moveTo(x=351, y=341, duration=0.5)
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

pyautogui.hotkey("ctrl", "alt", "t")
time.sleep(2)
pyautogui.hotkey('alt', 'f10')

pyautogui.write("nano", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(3)
pyautogui.click(clicks= 1)

pyautogui.hotkey("ctrl", "shift", "v")
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.hotkey("ctrl", "o")
time.sleep(2)

pyautogui.write("cotacao_dolar.txt", interval= 0.20)
pyautogui.press("ENTER")
pyautogui.hotkey("ctrl", "x")
time.sleep(2)

pyautogui.write("ls -l", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.write("rm cotacao_dolar.txt", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.write("ls -l", interval= 0.20)
pyautogui.press("ENTER")
time.sleep(2)

pyautogui.write("exit", interval= 0.20)
pyautogui.press("ENTER")
