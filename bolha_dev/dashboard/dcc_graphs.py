from ..database.database import Sqlite
from ..database.query_configs import query_configs
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc
sqlite = Sqlite()

DEFAULT_GRAPH_CLASS="drop-shadow-lg bg-white flex items-center rounded-2xl"

def create_dcc_grapth(id, fig):
    dcc_graph_count_posicao = dcc.Graph(
            id=id,
            style={'width': '60vh', 'height': '60vh'},
            figure=fig,
            config={
                'displayModeBar': False
            }
        )
    
    return dcc_graph_count_posicao

def create_df_from_query_file(query_config):
    query_path = query_config.get("query")
    columns = query_config.get("columns")
    count_posicao_query_result = sqlite.execute_query_by_path(query_path)
    df_count_posicao = pd.DataFrame(count_posicao_query_result, columns = columns)
    return df_count_posicao

df_count_posicao = create_df_from_query_file(query_configs['query_contagem_posicao'])
df_nivel_profissinal = create_df_from_query_file(query_configs['contagem_nivel_profissional'])
sqlite.cur.close()

query_contagem_nivel_profissional = '/home/linkedin-python-scrapy-scraper/database/contagem_nivel_profissional.sql'
fig_count_posicao = px.bar(
     df_count_posicao, 
     x="count_posicao", 
     y="posicao", 
     labels={
        "posicao": "Titulo Vaga","count_posicao": "Qtd vagas"
        },
     orientation='h', 
     title='Top 10 Posições',
     color=[
          "rgba(39, 0, 230, 0.8)", 
          "rgba(39, 30, 230, 0.8)", 
          "rgba(39, 60, 230, 0.8)",
          "rgba(39, 90, 230, 0.8)",
          "rgba(39, 120, 230, 0.8)",
          "rgba(39, 150, 230, 0.8)",
          "rgba(39, 180, 230, 0.8)",
          "rgba(39, 210, 230, 0.8)",
          "rgba(39, 240, 230, 0.8)",
          "rgba(39, 270, 230, 0.8)",
    ],
    
    color_discrete_map="identity",
)

fig_count_posicao.update_layout(
    yaxis=dict(
        autorange="reversed", 
        automargin='left',
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_family = "Lucida Console",
    title_x=0.5,
    #aqui é possível ajustar a distancia entre o label do eixo y e a margin da figur
    #essa valor foi ajustado pq o label da figura estava muito próximo da margin
    #da figura. dificultando a leitura.
    margin=dict(
        l=200,
    ),
)


dcc_graph_count_posicao = create_dcc_grapth('count-posicao', fig_count_posicao)
div_count_posicao = html.Div(children=[dcc_graph_count_posicao], className=DEFAULT_GRAPH_CLASS,)

c2 = create_dcc_grapth('c2', fig_count_posicao)
div_c2 = html.Div(children=[c2], className=DEFAULT_GRAPH_CLASS)

c3 = create_dcc_grapth('c3', fig_count_posicao)
div_c3 = html.Div(children=[c3], className=DEFAULT_GRAPH_CLASS)