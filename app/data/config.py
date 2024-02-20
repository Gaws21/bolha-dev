from app.config import Config
PREFIX_PATH = Config.ROOT_DIR

csv_configs = {
    "contagem_posicao":{
        "csv":f"{PREFIX_PATH}/app/data/contagem_posicao.csv",
        "columns":["attr","count_attr"]
    },
    "contagem_nivel_profissional":{
        "csv":f"{PREFIX_PATH}/app/data/contagem_nivel_profissional.csv",
        "columns":["attr","count_attr"]
    },
    "contagem_modalidade":{
        "csv":f"{PREFIX_PATH}/app/data/contagem_modalidade.csv",
        "columns":["attr","count_attr"]
    },
    "contagem_vagas_relevantes":{
        "csv":f"{PREFIX_PATH}/app/data/contagem_vagas_relevantes.csv",
        "columns":[ "attr", "count_attr"]
    },
    "contagem_por_dia_vs_modalidade":{
        "csv":f"{PREFIX_PATH}/app/data/contagem_por_dia_vs_modalidade.csv",
        "columns":["create_date", "count_day","hibrido","presencial","remoto"]
    },
    "job_links":{
        "csv":f"{PREFIX_PATH}/app/data/job_links.csv",
        "columns":["url_id", "title"]
    }
}