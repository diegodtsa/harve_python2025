from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o WebDriver automaticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Abrir o Google
driver.get("https://www.saucedemo.com/")

# Tempo para carregar a página
time.sleep(2)

login = driver.find_element(By.ID, 'user-name')
senha =  driver.find_element(By.ID, 'password')
botao = driver.find_element(By.ID, 'login-button')

login.send_keys('standard_user')
senha.send_keys('secret_sauce')
botao.click()

time.sleep(5)