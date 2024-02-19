PREFIX_PATH = "/home/bolha-dev/app/data"

query_configs = {
    "contagem_posicao":{
        "query":f"{PREFIX_PATH}/contagem_posicao.sql",
        "columns":["attr","count_attr"]
    },
    "contagem_nivel_profissional":{
        "query":f"{PREFIX_PATH}/contagem_nivel_profissional.sql",
        "columns":["attr","count_attr"]
    },
    "contagem_modalidade":{
        "query":f"{PREFIX_PATH}/contagem_modalidade.sql",
        "columns":["attr","count_attr"]
    },
    "contagem_vagas_relevantes":{
        "query":f"{PREFIX_PATH}/contagem_vagas_relevantes.sql",
        "columns":[ "attr", "count_attr"]
    },
    "count_por_dia_vs_modalidade":{
        "query":f"{PREFIX_PATH}/contagem_por_dia_vs_modalidade.sql",
        "columns":["create_date", "count_day","hibrido","presencial","remoto"]
    },
    "job_link":{
        "query":f"{PREFIX_PATH}/job_link.sql",
        "columns":["url_id", "title"]
    }
}