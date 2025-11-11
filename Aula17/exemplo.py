import pyautogui
import time

# Exibir o tamanho da tela
screen_width, screen_height = pyautogui.size()
print(f"Tamanho da tela: {screen_width}x{screen_height}")

# Mover o mouse para uma posição específica
pyautogui.moveTo(500, 500, duration=1)  # Move para x=500, y=500 em 1 segundo
print("Mouse Testando PyAutoGUI no Jupyter!Testando PyAutoGUI no Jupyter!movido!")

# Clicar no local atual
pyautogui.click()
print("Clique realizado!")

# Digitar um texto automaticamente
time.sleep(1)  # PeTestando PyAutoGUI no Jupyter!quena pausa antes de digitar
pyautogui.write("Testando PyAutoGUI no Jupyter!", interval=0.1)
print("Texto digitado!")

# Capturar a posição atual do mouse
x, y = pyautogui.position()
print(f"Posição atual do mouse: {x}, {y}")
