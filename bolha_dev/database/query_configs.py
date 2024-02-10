PREFIX_PATH = "/home/flask-hello-world/bolha_dev/database"

query_configs = {
    "query_contagem_posicao":{
        "query":f"{PREFIX_PATH}/query_contagem_posicao.sql",
        "columns":["posicao","count_posicao"]
    },
    "contagem_nivel_profissional":{
        "query":f"{PREFIX_PATH}/contagem_nivel_profissional.sql",
        "columns":["attr","count_attr"]
    },
    "contagem_modalidade":{
        "query":f"{PREFIX_PATH}/contagem_modalidade.sql",
        "columns":["attr","count_attr"]
    },
    "count_por_dia_vs_modalidade":{
        "query":f"{PREFIX_PATH}/count_por_dia_vs_modalidade.sql",
        "columns":["create_date", "count_day","hibrido","presencial","remoto"]
    }
}