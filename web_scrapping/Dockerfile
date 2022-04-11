# Dockerfile - Arquivo para construção de imagens
# Imagem - Template para construção de construção de container
# Container - Processo de imagem sendo executada

# Especificando imagem base com instalação de python
FROM python:3.8

# Adicionando arquivo .py do repositório atual no container
ADD web_scrapping.py .

# Rodando um comando no container para instalação das dependências
RUN pip install requests beautifulsoup4

# Comando que vai inicializar o container desse dockerfile
# Primeiro passamos o comando e depois o parâmetro
CMD ["python3", "/web_scrapping.py"]