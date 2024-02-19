from ..data.database import Sqlite
from ..data.config import query_configs
import pandas as pd

SQLITE = Sqlite()
JOB_LINKS = []

def format_percentage(float_value):
    float_formated = "{:.2f}".format(float_value)
    return float_formated

def create_df_from_query_file(query_config):
    query_path = query_config.get("query")
    columns = query_config.get("columns")
    count_posicao_query_result = SQLITE.execute_query_by_path(query_path)
    df_count_posicao = pd.DataFrame(count_posicao_query_result, columns = columns)
    return df_count_posicao

df_contagem_posicao = create_df_from_query_file(query_configs['contagem_posicao'])
df_nivel_profissinal = create_df_from_query_file(query_configs['contagem_nivel_profissional'])
df_contagem_modalidade = create_df_from_query_file(query_configs['contagem_modalidade'])
df_contagem_por_dia_vs_modalidade = create_df_from_query_file(query_configs['count_por_dia_vs_modalidade'])
df_contagem_vagas_relevantes = create_df_from_query_file(query_configs['contagem_vagas_relevantes'])
df_job_link = create_df_from_query_file(query_configs['job_link'])
SQLITE.cur.close()

vagas_coletadas= df_contagem_vagas_relevantes['count_attr'][0]
vagas_unicas= df_contagem_vagas_relevantes['count_attr'][1]
vagas_relevantes= df_contagem_vagas_relevantes['count_attr'][2]

percentual_coletados_x_unicas = 1-(int(vagas_unicas)/int(vagas_coletadas))
percentual_coletados_x_relevantes = 1-(int(vagas_relevantes)/int(vagas_coletadas))

percentual_formatado = format_percentage(percentual_coletados_x_unicas)
percentual_formatado_relevantes = format_percentage(percentual_coletados_x_relevantes)

for job_link in df_job_link.itertuples():
    JOB_LINKS.append((job_link.url_id, job_link.title))
