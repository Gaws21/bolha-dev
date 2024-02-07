"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template, request


@app.route("/")
def home():
    """Home page of Flask Application."""

    #as informações de title, description e template vão fazer parte das infos de metadata da página html index
    #não identifiquei onde foi para a mensagem do body
    return render_template("base_layout.jinja2")
