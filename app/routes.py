from flask import current_app as app
from flask import render_template, request
from .data.data import *
from app.config import user_agent_configs
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
search_results = JOB_LINKS
list_pagination = []
user_agent_config = None
@app.route("/")
def home():
    user_agent = request.user_agent.string.lower()
    device = "mobile"
    if not device in user_agent:
        device="desktop"
    
    global user_agent_config
    user_agent_config = user_agent_configs.get(device)
    kwargs = {
        "labels": list(df_contagem_posicao["attr"]),
        "values": list(df_contagem_posicao["count_attr"]),
        "labels1": list(df_nivel_profissinal['attr']),
        "values1": list(df_nivel_profissinal['count_attr']),
        "labels_modalidade":list(df_contagem_modalidade['attr']), \
        "values_modalidade":list(df_contagem_modalidade['count_attr']), \
        "labels_historico":list(df_contagem_por_dia_vs_modalidade['create_date']), \
        "modalidade_total_presencial":list(df_contagem_por_dia_vs_modalidade['presencial']),\
        "modalidade_total_hibrido":list(df_contagem_por_dia_vs_modalidade['hibrido']),\
        "modalidade_total_remoto":list(df_contagem_por_dia_vs_modalidade['remoto']),\
        "vagas_coletadas": df_contagem_vagas_relevantes['count_attr'][0],\
        "vagas_unicas": df_contagem_vagas_relevantes['count_attr'][1],\
        "vagas_relevantes": df_contagem_vagas_relevantes['count_attr'][2],\
        "percentual_unicas": percentual_formatado,\
        "percentual_relevantes": percentual_formatado_relevantes
    }
    return render_template(user_agent_config.get("home_page"), **kwargs)


@app.route("/search-jobs")
def search_table():
    page_numbers = len(JOB_LINKS)//user_agent_config.get("pagination_size")+2
    modulus_page_number = len(JOB_LINKS)%user_agent_config.get("pagination_size")
    if modulus_page_number == 0:
        page_numbers-=1
    global list_pagination
    list_pagination = range(1, page_numbers)
    return render_template(user_agent_config.get("first_result_page"), results=JOB_LINKS[0:user_agent_config.get("pagination_size")], pages=list_pagination, current_page=1)

@app.route("/get-results")
def get_results():
    q = request.args.get("q")
    if q:
        search_result_jobs = []
        for result in JOB_LINKS:
            if q.lower() in result[1].lower():
                search_result_jobs.append(result)
    else:
        search_result_jobs = JOB_LINKS
    
    global search_results
    search_results = search_result_jobs
    page_numbers = len(search_results)//user_agent_config.get("pagination_size")+2
    modulus_page_number = len(search_results)%user_agent_config.get("pagination_size")
    if modulus_page_number == 0:
        page_numbers-=1
    global list_pagination
    list_pagination = range(1, page_numbers)

    if len(search_results) == 0:
        list_pagination = []

    return render_template(user_agent_config.get("search_result_page"), results=search_results[0:user_agent_config.get("pagination_size")], pages=list_pagination, current_page=1)

@app.route("/get-page")
def next_page():
    page = request.args.get("page")
    final_page = int(page)*user_agent_config.get("pagination_size")
    initial_page = final_page-user_agent_config.get("pagination_size")
    return render_template(user_agent_config.get("search_result_page"), results=search_results[initial_page:final_page], pages=list_pagination, current_page=int(page))
