from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar o WebDriver automaticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrir o Google
driver.get("https://www.google.com")

# Fechar o navegador
time.sleep(2)
driver.quit()
print("Chrome fechado com sucesso!")