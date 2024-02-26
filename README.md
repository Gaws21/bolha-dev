# Bolha Dev 
![Screenshot](https://github.com/Gaws21/Gaws21/blob/main/bolha-dev-1.png)
![Screenshot](https://github.com/Gaws21/Gaws21/blob/main/bolha-dev-2.png)
![Screenshot](https://github.com/Gaws21/Gaws21/blob/main/bolha-dev-3.png)

https://bolha-dev.onrender.com/

[PT-BR]

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

Os valores nos gráficos sempre são referentes aos dados coletados na última pesquisa.
Um combilado dos valores macros históricos estão apresentados no último gráfico `Historico`.

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
    gunicorn app:app 
    ```
 - Para sair do ambiente virtual:
    ```
    deactivate
    ```

[ENGLISH]

This project was born as a way to explore and develop my skills in 
web development, creation of dashboards and data analysis. After starting to analyze the advertised vacancies
on LinkedIn in the last 24 hours, I identified that the real numbers that match the terms
of the research are much smaller than those presented. As a way to better analyze the
IT market and create a small portfolio decides to develop this application by
use of the following stack:

 - flask
 - chartjs
 - htmx
 - tailwind

The values in the graphs always refer to the data collected in the last search.
A combination of historical macro values are presented in the last `History` graph.

If you are a beginner and don't have much experience with Python or Git, don't feel bad.
It's quite simple. After cloning the project, open a terminal in the project folder and follow the instructions
instructions below:

- Create a virtual environment
    ```
    python3 -m venv .venv
    ```
 - Activate venv:
    ```
    source .venv/bin/activate
    ```
 - Install requirements:
    ```
    pip install -r requirements
    ```
 - Run app Flaks with gunicorn:
    ```
    gunicorn app:app 
    ```
 - Deactivate virtual env:
    ```
    deactivate
    ```