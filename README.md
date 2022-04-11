# Docker Projetos

Esse repositório é produto de práticas realizadas durante o aprendizado de docker. A linguagem de programação usada durante as práticas foi o Python. 

Mais do que um repositório para Docker com códigos que usam Python também é um repositório que traz um pouco dos resultados de pesquisas sobre a aplicação de Container em Ciência de Dados, mais especificamente no isolamento de ambiente de execução e escalonamento de aplicações de Ciência de Dados.

As três pastas desse repositório envolvem:

1. Aplicação estática que usa o container puramente como ambiente de execução: web_scrapping
2. Aplicação interativa que usa o container para isolar o ambiente mas requer resposta: adivinha_numero
3. API para usar um modelo de ML isolado em um container: iris_ml
4. Criando ambiente de ciência de dados usando um container: ambiente

web_scrapping.py:    
1. Para construir o container: `docker build -t python-ml-ws .`
2. Para rodar o container: `docker run python-ml-ws`

adivinha_numero.py:
1. Para construir o container: `docker build -t python-adivinha_numero .`
2. Para rodar o container: `docker run -t -i python-adivinha_numero`

iris_ml.py:
1. Para rodar a API: `python3 app.py`
2.    Para construir o container: `docker build -t python-iris .`
3.    Para rodar o container: `docker run -t python-iris`

ambiente:
1. Rodar a imagem base do doscker hub com anaconda: `docker run -it -p xxxx:xxxx -v "$PWD/notebooks:/home" continuumio/anaconda3 /bin/bash`
2. Criar jupyter notebook dentro do container criado: `jupyter notebook --ip='*' --port=xxxx --no-browser --allow-root`
3. Buildar imagem customizada com apenas alguns pacotes: `docker build -t image_ambiente .`
4. Executar imagem customizada: `docker run -d --rm --name jupyterserver -p xxxx:xxxx -v "$PWD/notebooks:/home/notebooks" image_ambiente`
    
Sobre o ambiente para data science:
* -it, permite usar o container de forma iterativa
* -p, mapeamento das portas do container da máquina 
* -v, faz o mapeamento de diretórios entre o container e a máquina
* -d, constroi o container de forma desanexada, sem bloquear a linha de comando
* --rm, limpa containers antigos que usem a mesma imagem 
* --name, define um nome para o container

