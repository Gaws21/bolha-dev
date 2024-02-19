PREFIX_PATH = "/home/bolha-dev/app/data"

csv_configs = {
    "contagem_posicao":{
        "csv":f"{PREFIX_PATH}/contagem_posicao.csv",
        "columns":["attr","count_attr"]
    },
    "contagem_nivel_profissional":{
        "csv":f"{PREFIX_PATH}/contagem_nivel_profissional.csv",
        "columns":["attr","count_attr"]
    },
    "contagem_modalidade":{
        "csv":f"{PREFIX_PATH}/contagem_modalidade.csv",
        "columns":["attr","count_attr"]
    },
    "contagem_vagas_relevantes":{
        "csv":f"{PREFIX_PATH}/contagem_vagas_relevantes.csv",
        "columns":[ "attr", "count_attr"]
    },
    "contagem_por_dia_vs_modalidade":{
        "csv":f"{PREFIX_PATH}/contagem_por_dia_vs_modalidade.csv",
        "columns":["create_date", "count_day","hibrido","presencial","remoto"]
    },
    "job_links":{
        "csv":f"{PREFIX_PATH}/job_links.csv",
        "columns":["url_id", "title"]
    }
}