from flask import current_app as app
from flask import render_template, request
from .data.data import *

search_results = JOB_LINKS
list_pagination = []

@app.route("/")
def home():
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
    return render_template("home_copy.html", **kwargs)


@app.route("/search-jobs")
def search_table():
    page_numbers = len(JOB_LINKS)//16+1 
    global list_pagination
    list_pagination = range(1, page_numbers)
    return render_template("first_results_mobile.html", results=JOB_LINKS[0:56], pages=list_pagination)

@app.route("/get-results")
def get_results():
    q = request.args.get("q")
    if q:
        search_results = []
        for result in JOB_LINKS:
            if q.lower() in result[1].lower():
                search_results.append(result)
    else:
        search_results = JOB_LINKS

    page_numbers = len(search_results)//16+1 
    global list_pagination
    list_pagination = range(1, page_numbers)

    if len(search_results) == 0:
        list_pagination = []

    return render_template("search_results.html", results=search_results[0:16], pages=list_pagination)

@app.route("/get-page")
def next_page():
    page = request.args.get("page")
    final_page = int(page)*16
    initial_page = final_page-16
    
    return render_template("search_results.html", results=search_results[initial_page:final_page], pages=list_pagination)