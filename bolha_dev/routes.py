"""Routes for parent Flask app."""
import pdb
from flask import current_app as app
from flask import render_template, request
from .dashboard.dcc_graphs import df_count_posicao


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
    return render_template("base_layout.jinja2", labels=labels_list, values=values_list)
