"""Routes for parent Flask app."""
import pdb
from flask import current_app as app
from flask import render_template, request
from bolha_dev import db
from bolha_dev import Joblinks
from .database.df_data import df_contagem_vagas_relevantes, df_count_posicao, df_nivel_profissinal, df_contagem_modalidade, df_count_por_dia_vs_modalidade


results = db.session.execute(db.select(Joblinks.url_id, Joblinks.title)).all()
results_list = []
global search_results
search_results = []

list_pagination = None
for result in results:
    results_list.append((result.url_id, result.title))

search_results = results_list
@app.route("/")
def home():
    """Home page of Flask Application."""
    data = [
        ("01-01-2024",1234),
        ("02-01-2024",1235),
        ("03-01-2024",1236),
        ("04-01-2024",1237),
        ("05-01-2024",1238),
        ("06-01-2024",1239),
        ("07-01-2024",1230),
        ("08-01-2024",1231),
        ("09-01-2024",1232),
        ("10-01-2024",1233),
    ]
    labels = df_count_posicao["posicao"]
    values = df_count_posicao["count_posicao"]

    labels_list = [label for label in labels]
    values_list = [value for value in values]

    #as informações de title, description e template vão fazer parte das infos de metadata da página html index
    #não identifiquei onde foi para a mensagem do body

    vagas_coletadas= df_contagem_vagas_relevantes['count_attr'][0]
    vagas_unicas= df_contagem_vagas_relevantes['count_attr'][1]
    vagas_relevantes= df_contagem_vagas_relevantes['count_attr'][2]

    percentual_coletados_x_unicas = 1-(vagas_unicas/vagas_coletadas)

    percentual_coletados_x_relevantes = 1-(vagas_relevantes/vagas_coletadas)

    percentual_formatado = "{:.2f}".format(percentual_coletados_x_unicas)
    percentual_formatado_relevantes = "{:.2f}".format(percentual_coletados_x_relevantes)
    return render_template("html_teste.html", \
                           labels=labels_list, \
                            values=values_list, \
                                labels1=list(df_nivel_profissinal['attr']), \
                                    values1=list(df_nivel_profissinal['count_attr']),\
                                        labels_modalidade=list(df_contagem_modalidade['attr']), \
                                            values_modalidade=list(df_contagem_modalidade['count_attr']), \
                                                labels_historico=list(df_count_por_dia_vs_modalidade['create_date']), \
                                                        modalidade_total_presencial=list(df_count_por_dia_vs_modalidade['presencial']),\
                                                            modalidade_total_hibrido=list(df_count_por_dia_vs_modalidade['hibrido']),\
                                                                modalidade_total_remoto=list(df_count_por_dia_vs_modalidade['remoto']),\
                                                                    vagas_coletadas= df_contagem_vagas_relevantes['count_attr'][0],\
                                                                        vagas_unicas= df_contagem_vagas_relevantes['count_attr'][1],\
                                                                            vagas_relevantes= df_contagem_vagas_relevantes['count_attr'][2],\
                                                                                percentual_unicas=percentual_formatado,\
                                                                                    percentual_relevantes=percentual_formatado_relevantes)

@app.route("/test-title")
def test_title():
    """Home page of Flask Application."""
    data = [
        ("01-01-2024",1234),
        ("02-01-2024",1235),
        ("03-01-2024",1236),
        ("04-01-2024",1237),
        ("05-01-2024",1238),
        ("06-01-2024",1239),
        ("07-01-2024",1230),
        ("08-01-2024",1231),
        ("09-01-2024",1232),
        ("10-01-2024",1233),
    ]
    labels = df_count_posicao["posicao"]
    values = df_count_posicao["count_posicao"]

    labels_list = [label for label in labels]
    values_list = [value for value in values]

    #as informações de title, description e template vão fazer parte das infos de metadata da página html index
    #não identifiquei onde foi para a mensagem do body
    return render_template("html_title.html", \
                           labels_historico=list(df_count_por_dia_vs_modalidade['create_date']), \
                            modalidade_total_presencial=list(df_count_por_dia_vs_modalidade['presencial']),\
                                modalidade_total_hibrido=list(df_count_por_dia_vs_modalidade['hibrido']),\
                                    modalidade_total_remoto=list(df_count_por_dia_vs_modalidade['remoto']))

@app.route('/test-db')
def db_test():
    try:
        job_links = db.session.execute(db.select(Joblinks.job_link)).scalars()


        sock_text = '<ul>'
        for job in job_links:
            sock_text += '<li>' + job + '</li>'
        sock_text += '</ul>'
        return sock_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/search-jobs")
def search_table():
    page_numbers = len(results_list)//16+1 

    global list_pagination
    list_pagination = range(1, page_numbers)
    return render_template("first_results.html", results=results_list[0:16], pages=list_pagination)

@app.route("/get-results")
def get_results():
    q = request.args.get("q")
    if q:
        search_results = []
        for result in results_list:
            if q.lower() in result[1].lower():
                search_results.append(result)
    else:
        search_results = results_list

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