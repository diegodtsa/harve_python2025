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
driver.get("https://www.mercadolivre.com")
driver.maximize_window()


# Tempo para carregar a página
time.sleep(2)

pesquisar = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]')
pesquisar.send_keys("Notebook Dell")
pesquisar.submit()
time.sleep(2)

actions = ActionChains(driver).scroll_to_element(element='//*[@id="root-app"]/div/div[2]/section/div[4]/nav/ul/li[12]')
botao_seguinte = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[4]/nav/ul/li[12]')
time.sleep(3)

botao_seguinte = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[4]/nav/ul/li[12]')
time.sleep(3)

clicar = driver.find_element(By.CLASS_NAME, 'ui-search-result__wrapper')
clicar.click()
time.sleep(3)