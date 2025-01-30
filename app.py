import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Cargar datos
df = pd.read_csv("/mnt/data/ds.csv")

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Gráfico de barras de favoritos por país
fig_favorites = px.bar(df, x='country', y='favorites', title='Número de Me Gusta por País',
                        labels={'favorites': 'Favoritos', 'country': 'País'},
                        color='country')

# Gráfico de dispersión seguidores vs seguidos
fig_followers = px.scatter(df, x='followers', y='followees', color='country',
                           title='Relación entre Seguidores y Seguidos',
                           labels={'followers': 'Seguidores', 'followees': 'Seguidos'})

# Diseño del dashboard
app.layout = html.Div(children=[
    html.H1("Dashboard de Redes Sociales"),
    dcc.Graph(id='favorites-graph', figure=fig_favorites),
    dcc.Graph(id='followers-graph', figure=fig_followers)
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
