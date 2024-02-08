PREFIX_PATH = "/home/flask-hello-world/bolha_dev/database"

query_configs = {
    "query_contagem_posicao":{
        "query":f"{PREFIX_PATH}/query_contagem_posicao.sql",
        "columns":["posicao","count_posicao"]
    },
    "contagem_nivel_profissional":{
        "query":f"{PREFIX_PATH}/contagem_nivel_profissional.sql",
        "columns":["attr","count_attr"]
    }
}