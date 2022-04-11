from bs4 import BeautifulSoup
import requests

# Abaixo fazemos uma requisição para o site do mercadolivre
site = requests.get('https://lista.mercadolivre.com.br/capa-de-celular#D[A:capa%20de%20celular]').content

# Objeto soup baixando o html do site
soup = BeautifulSoup(site, 'html.parser')

# Transforma html em string e o print vai exibir o html
# print(soup.prettify())

# Encontrando os preços no html
lista = soup.find_all("span", class_ = "price-tag-amount")

# Imprimindo os preços dos produtos
for produto in lista:
    preco = produto.find("span", class_ = "price-tag-fraction").text
    print(f'R$ {preco}')