import requests
from bs4 import BeautifulSoup
from lxml import html

url = 'https://valor.globo.com/valor-data/'

response = requests.get(url)

objeto = html.fromstring(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find('div', class_='cell auto data-cotacao__ticker_quote').get_text()

print(links)

#titulo = objeto.xpath('string(//*[@id="fundo"]/div[1]/div[2]/div/div/div[5]/div/p)')

#print(titulo.strip())