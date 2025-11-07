import requests
from bs4 import BeautifulSoup
from lxml import html

url = 'https://www.harve.com.br'

response = requests.get(url)

objeto = html.fromstring(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')

for site in links:
    if site.get('href'):
        print(site.text)
        print(site.get('href'))

print(links)

#titulo = objeto.xpath('string(//*[@id="fundo"]/div[1]/div[2]/div/div/div[5]/div/p)')

#print(titulo.strip())