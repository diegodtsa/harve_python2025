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

# Abrir o Google
driver.get("https://form.respondi.app/WlvJ2EEh")
driver.maximize_window()

# Tempo para carregar a página
time.sleep(2)

nome = driver.find_element(By.XPATH, '//*[@id="988d86bfb8b0-input"]')
nome.send_keys('Diego Teixeira')
nome.send_keys(Keys.ENTER)
time.sleep(2)

telefone = driver.find_element(By.XPATH, '//*[@id="xi29fyr0s5y-input"]')
telefone.send_keys('92 98185-9675')
telefone.send_keys(Keys.ENTER)
time.sleep(2)

email = driver.find_element(By.XPATH, '//*[@id="xe6erhg1bvw-input"]')
email.send_keys('diego.dtsa@gmail.com')
email.send_keys(Keys.ENTER)
time.sleep(5)