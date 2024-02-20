# Bolha Dev 

Esse projeto nasceu como uma forma de explorar e desenvolver habilidades com desenvolvimento
web, criação de dashboards e análise de dados. Após começar analisar as vagas divulgadas
no linkedin nas últimas 24h, identifiquei que os números reais que condizem com os termos
da pesquisa são bem menores do que os apresentados. Como uma forma de analisar melhor o 
mercado de ti e criar um pequeno portfólio resolvi desenvolver essa aplicação fazendo
uso da seguinte stack:

 - flask
 - chartjs
 - htmx
 - tailwind

Os dados são referente a coletas com os termos:
 - engenheiro de dados
 - data engineer
 - python developer
 - python desenvolvedor
 - python programador
 - desenvolvedor python
 - programador python

As pesquisas foram feitas de maneira aleatória. Normalmente com intervalos de 2 dias.
Todas as pesquisas estão restringidas as regiões de Brasil em modalidade remota e 
São Paulo em todas modalidades.

# Como rodar ? 
Caso você seja iniciante e não tenha muita experiência com python ou git não se sinta mal.
É bem simples. Após clonar o projeto, abra um terminal na pasta do projeto e siga as
instruções abaixo:

 - Crie um ambiente virtual 
    ```
    python3 -m venv .venv
    ```
 - Ative o venv:
    ```
    source .venv/bin/activate
    ```
 - Instale as dependências:
    ```
    pip install -r requirements
    ```
 - Execute a aplicação flask:
    ```
    python3 run.py
    ```
 - Para sair do ambiente virtual:
    ```
    deactivate
    ```