from bolha_dev import init_app

#retorna o objeto app inicializados
app = init_app()

#inicializa a aplicação
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083, debug=True, load_dotenv=True)