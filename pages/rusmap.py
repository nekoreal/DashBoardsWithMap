from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

from data import df_region, counties

rusmap = px.choropleth_map(
    df_region,
    geojson=counties,
    featureidkey='properties.cartodb_id',
    color='ВВП на душу населения',
    locations='cartodb_id',
    color_continuous_scale=px.colors.sequential.Teal,
    map_style="carto-positron",
    zoom=1,
    center={"lat": 66, "lon": 94},
    opacity=0.5,
    hover_name='region',
    hover_data={'region': True, 'cartodb_id': False},
    labels={'region': 'Субъект РФ'}
)

rusmap.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=500,
    showlegend=False
)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H3("Карта регионов Российской федерации"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'})
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=rusmap)
        ], width=12),
    ]),
])