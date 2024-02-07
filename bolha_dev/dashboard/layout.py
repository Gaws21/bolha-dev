"""Plotly Dash HTML layout override."""

html_layout = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        {%metas%}
        <title>Página de dashs</title>
        {%css%}
    </head>

    <body>
    <div class="items-center justify-center pl-2 border h-12">
        <img src="../static/images/logo_bolha_dev.svg" width=13% height=13% class="p-2"/>
        </div>
        <section class="flex h-screen bg-zinc-200 ">
        <aside class="w-55   bg-white p-6">
            <nav class="mt-5 space-y-3">
            <a href="#" class="bg-white/10 group rounded flex items-center gap-4 overflow-hidden hover:bg-zinc-400 transition-colors">
                <img src="../static/images/bar_chart.png" width=20% width=20% />
                Home</a>
                <a href="#" class="bg-white/10 group rounded flex items-center gap-4 overflow-hidden hover:bg-zinc-400 transition-colors">
                <img src="../static/images/search_more.png" width=20% width=20% />
                Search Jobs</a>
            </nav>
        </aside>
        <main class="flex-1 p-6 ">
            {%app_entry%}
        </main>
        </section>
        <footer class="h-8 border">
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
    </html>
"""
