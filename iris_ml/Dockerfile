# Imagem base de python
FROM python:3.8

# Diretório de trabalho do container
WORKDIR /code

# Cópia arquivo de dependências para o WORKDIR do container
COPY requirements.txt .

# Instala as dependdências
RUN pip install -r requirements.txt

# Copia o conteúdo do diretório para o WORKDIR
COPY . .

# Comando a ser rodado quando o container startar
CMD [ "python", "./app.py" ]

# Para construir a imagem use: docker build -t iris-rf-app .
# Depois de construir a imagem você pode rodar o container usando: docker run -d -p 5001:5001 iris-rf-app