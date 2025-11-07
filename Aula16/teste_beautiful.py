#source .venv/bin/activate

import requests
from bs4 import BeautifulSoup


#url = 'https://www.saucedemo.com'
#url = 'https://www.amazon.com'
#url = 'https://www.globo.com'
url = 'https://www.mercadolivre.com'
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
else:
    print(response.status_code)
