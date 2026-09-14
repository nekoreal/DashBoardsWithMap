from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df, all_cont

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H3("Подробная информация о выбранной стране"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'})
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.P("Выберите континент:", style={'margin': 'auto 0', 'fontWeight': '500'})
        ], width=2, style={'display': 'flex', 'alignItems': 'center'}),
        dbc.Col([
            dcc.Dropdown(
                id='crossfilter-cont',
                options=[{'label': i, 'value': i} for i in all_cont],
                value=all_cont[0],
                multi=False
            )
        ], width=3),
        dbc.Col([
            html.P("Выберите страну:", style={'margin': 'auto 0', 'fontWeight': '500'})
        ], width=2, style={'display': 'flex', 'alignItems': 'center'}),
        dbc.Col([
            dcc.Dropdown(
                id='crossfilter-count',
                multi=False
            )
        ], width=3)
    ], style={'alignItems': 'center'}),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Уровень жизни", style={'backgroundColor': '#f8f9fa', 'fontSize': '14px', 'padding': '6px'}),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/money.png', style={'maxHeight': '55px', 'width': 'auto'})
                    ], width=4, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(id='card_text1', className="card-value", style={'fontSize': '16px', 'fontWeight': 'bold', 'margin': 0}),
                            style={'padding': '10px'}
                        )
                    ], width=8, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                ], className="g-0", style={'height': '70px'})
            ], style={'border': '1px solid #20c997', 'borderRadius': '6px', 'overflow': 'hidden', 'textAlign': 'center'}),
        ], width=3),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Численность населения", style={'backgroundColor': '#f8f9fa', 'fontSize': '14px', 'padding': '6px'}),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/religious.png', style={'maxHeight': '55px', 'width': 'auto'})
                    ], width=4, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(id='card_text2', className="card-value", style={'fontSize': '16px', 'fontWeight': 'bold', 'margin': 0}),
                            style={'padding': '10px'}
                        )
                    ], width=8, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                ], className="g-0", style={'height': '70px'})
            ], style={'border': '1px solid #ff6b6b', 'borderRadius': '6px', 'overflow': 'hidden', 'textAlign': 'center'}),
        ], width=3),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Образование", style={'backgroundColor': '#f8f9fa', 'fontSize': '14px', 'padding': '6px'}),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/diploma.png', style={'maxHeight': '55px', 'width': 'auto'})
                    ], width=4, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(id='card_text3', className="card-value", style={'fontSize': '16px', 'fontWeight': 'bold', 'margin': 0}),
                            style={'padding': '10px'}
                        )
                    ], width=8, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                ], className="g-0", style={'height': '70px'})
            ], style={'border': '1px solid #868e96', 'borderRadius': '6px', 'overflow': 'hidden', 'textAlign': 'center'}),
        ], width=3),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Статус", style={'backgroundColor': '#f8f9fa', 'fontSize': '14px', 'padding': '6px'}),
                dbc.Row([
                    dbc.Col([
                        dbc.CardImg(src='/static/images/globe.png', style={'maxHeight': '55px', 'width': 'auto'})
                    ], width=4, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                    dbc.Col([
                        dbc.CardBody(
                            html.P(id='card_text4', className="card-value", style={'fontSize': '16px', 'fontWeight': 'bold', 'margin': 0}),
                            style={'padding': '10px'}
                        )
                    ], width=8, style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
                ], className="g-0", style={'height': '70px'})
            ], style={'border': '1px solid #339af0', 'borderRadius': '6px', 'overflow': 'hidden', 'textAlign': 'center'}),
        ], width=3)
    ]),

    html.Br(),

    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H5("Уровень ВВП по странам континента на 2015 год"),
                dcc.Graph(id='choropleth1', config={'displayModeBar': False}),
            ], width=8),
            dbc.Col([
                dbc.Row([
                    html.Div(id='card1')
                ], style={'marginBottom': '15px'}),
                html.Br(),
                dbc.Row([
                    html.H5("ТОП-5 стран по ВВП", style={'textAlign': 'center', 'fontSize': '16px', 'fontWeight': 'bold', 'marginBottom': '10px'}),
                    html.Div(id='table1')
                ], style={"textAlign":"center"})
            ], width=4)
        ]),
    ])
], fluid=True)


@callback(
    [Output('crossfilter-count', 'options'),
     Output('crossfilter-count', 'value')],
    Input('crossfilter-cont', 'value')
)
def update_region(cont):
    all_count = df[(df['continent'] == cont)]['Country'].unique()
    dd_count = [{'label': i, 'value': i} for i in all_count]
    dd_count_value = all_count[0]
    return dd_count, dd_count_value

@callback(
    [Output('card_text1', 'children'),
     Output('card_text2', 'children'),
     Output('card_text3', 'children'),
     Output('card_text4', 'children'),
     Output('card1', 'children'),
     Output('table1', 'children'),
     Output('choropleth1', 'figure')],  
    [Input('crossfilter-count', 'value'),
     Input('crossfilter-cont', 'value')]
)
def update_card(count, cont):
    df_count = df[(df['Country'] == count) & (df['Year'] == 2015)]
    df_count14 = df[(df['Country'] == count) & (df['Year'] == 2014)]
    gdp_count = df[(df['continent'] == cont) & (df['Year'] == 2015)].sort_values(by='GDP', ascending=False)

    ct1 = df_count.iloc[0]['Life expectancy']
    ct2 = df_count.iloc[0]['Population']
    ct3 = df_count.iloc[0]['Schooling']
    ct4 = df_count.iloc[0]['Status']
    gdp15 = df_count.iloc[0]['GDP']
    gdp14 = df_count14.iloc[0]['GDP']

    gdp_table = gdp_count.iloc[0:5][['Country', 'GDP']]
    delta_gdp = round((gdp15 - gdp14) / gdp14, 2) * 100

    # Динамика ВВП
    if delta_gdp > 0:
        delta_text = f"▲ +{delta_gdp:.0f}%"
        delta_color = "green"
    elif delta_gdp < 0:
        delta_text = f"▼ {delta_gdp:.0f}%"
        delta_color = "red"
    else:
        delta_text = f"{delta_gdp:.0f}%"
        delta_color = "gray"

    card1 = dbc.Card([
        dbc.CardHeader("Валовый внутренний продукт", style={'backgroundColor': '#f8f9fa', 'fontSize': '14px', 'padding': '6px'}),
        dbc.CardBody([
            html.H4(gdp15, style={'fontWeight': 'bold', 'marginBottom': '5px'}),
            html.Div(delta_text, style={'fontSize': '16px', 'fontWeight': 'bold', 'color': delta_color}),
            html.I('в % к 2014 году', style={'fontSize': '13px', 'color': '#6c757d'})
        ], style={'padding': '12px'})
    ], style={'textAlign': 'center', 'border': '1px solid #ced4da', 'borderRadius': '6px', 'overflow': 'hidden'})

    table = dbc.Table.from_dataframe(
        gdp_table, 
        striped=True, 
        bordered=True, 
        hover=True, 
        index=False,
        style={'textAlign': 'center', 'fontSize': '13px'}
    )

    # Генерация Choropleth карты
    figure = px.choropleth(
        gdp_count,
        locations='Country',
        locationmode='country names',
        color="GDP",
        hover_name='Country',
        hover_data={
            'Country': True,
            'Year': False,
            'Status': False,
            'Life expectancy': True,
            'Population': True,
            'GDP': True,
            'Schooling': False,
            'continent': False,
        },
        labels={
            'Country': 'Страна',
            'Year': 'Год',
            'Population': 'Население',
            'Life expectancy': 'Продолжительность жизни',
            'GDP': 'ВВП',
            'Schooling': 'Продолжительность обучения',
        },
        color_continuous_scale=px.colors.sequential.Teal,
    )

    figure.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        showlegend=False,
        coloraxis_showscale=False,
    )

    return ct1, ct2, ct3, ct4, card1, table, figure