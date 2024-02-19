from ..database.database import Sqlite
from ..database.query_configs import query_configs
import pandas as pd
sqlite = Sqlite()

def create_df_from_query_file(query_config):
    query_path = query_config.get("query")
    columns = query_config.get("columns")
    count_posicao_query_result = sqlite.execute_query_by_path(query_path)
    df_count_posicao = pd.DataFrame(count_posicao_query_result, columns = columns)
    return df_count_posicao

df_count_posicao = create_df_from_query_file(query_configs['query_contagem_posicao'])
df_nivel_profissinal = create_df_from_query_file(query_configs['contagem_nivel_profissional'])
df_contagem_modalidade = create_df_from_query_file(query_configs['contagem_modalidade'])
df_count_por_dia_vs_modalidade = create_df_from_query_file(query_configs['count_por_dia_vs_modalidade'])
df_contagem_vagas_relevantes = create_df_from_query_file(query_configs['contagem_vagas_relevantes'])

sqlite.cur.close()