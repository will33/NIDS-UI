import json
import pandas as pd
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# Configure Dash app
app = dash.Dash(__name__, title='NIDS')
# external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']

app.layout = html.Div(children=[

    # Titles
    html.Div(
        children=[
            html.H1(
                children='NIDS UI',
                style={
                    'background': '#326ba8',
                    'color': 'white',
                    'padding-top': '5vh',
                    'padding-bottom': '5vh'
                }
            ),
            html.Div(
                [
                    html.Div(
                        html.Button(
                            'Visualise data',
                            id='data-visualisation-toggle', 
                            n_clicks=0
                        ),
                        className='three columns',
                        style={
                            'textAlign': 'center',
                            'margin-top': '4px'
                        }
                    ),
                    html.Div(
                        html.H2(
                            'Data visualisation dashboard',
                            id='page-title',
                            style={
                                'margin': '0px',
                            }
                        ),
                        className='six columns',
                        style={
                            'margin-top': '0px',
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        html.Button(
                            'Explore NIDS',
                            id='nids-toggle',
                            n_clicks=0,
                        ),
                        className='three columns',
                        style={
                            'textAlign': 'center',
                            'margin-top': '4px'
                        }
                    )
                ],
                className='row',
                style={
                    'margin-bottom': '3rem',
                    'textAlign': 'center'
                }
            ),
        ],
        style={
            'textAlign': 'center'
        }
    ),

    # Data visualisation page
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H3('Packet IP addresses'),
                            dcc.Graph(id='graph-1'),
                        ],
                        className='six columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        [
                            html.H3('Graph 2'),
                            dcc.Graph(id='graph-2'),
                        ],
                        className='six columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                ],
                className='row'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='feature-dropdown',
                                options=[
                                    {'label': 'Source IPs', 'value': 'IPV4_SRC_ADDR'},
                                    {'label': 'Destination IPs', 'value': 'IPV4_DST_ADDR'}
                                ],
                                value='IPV4_SRC_ADDR',
                                multi=False
                            ),
                        ],
                        className='two columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='region_selection',
                                options=[
                                    {'label': 'Queensland', 'value': 'QLD1'},
                                    {'label': 'New South Wales', 'value': 'NSW1'},
                                    {'label': 'Victoria', 'value': 'VIC1'},
                                    {'label': 'South Australia', 'value': 'SA1'},
                                    {'label': 'Tasmania', 'value': 'TAS1'},
                                ],
                                value=['QLD1'],
                                multi=True,
                            ),
                        ],
                        className='two columns'
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='nem_period_selection',
                                options=[
                                    {'label': 'Day of week', 'value': 'day_of_week'},
                                    {'label': 'Day of month', 'value': 'day_of_month'},
                                    {'label': 'Day of year', 'value': 'day_of_year'},
                                    {'label': 'Week', 'value': 'week'},
                                    {'label': 'Month', 'value': 'month'}
                                ],
                                value='month',
                                multi=False
                            ),
                        ],
                        className='two columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='product_selection',
                                options=[
                                    {'label': 'Futures', 'value': 'Future'},
                                    {'label': 'Caps', 'value': 'Cap'},
                                    {'label': 'Options', 'value': 'Option'}
                                ],
                                value=['Future', 'Cap', 'Option'],
                                multi=True,
                            ),
                        ],
                        className='three columns',
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='asx_period_selection',
                                options=[
                                    {'label': 'Day of week', 'value': 'day_of_week'},
                                    {'label': 'Day of month', 'value': 'day_of_month'},
                                    {'label': 'Day of year', 'value': 'day_of_year'},
                                    {'label': 'Week', 'value': 'week'},
                                    {'label': 'Month', 'value': 'month'}
                                ],
                                value='month',
                                multi=False,
                            ),
                        ],
                        className='two columns',
                        style={
                            'textAlign': 'center',
                            'margin-left': '8vw'
                        }
                    )
                ],
                className='row'
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.H4('Graph 3'),
                            dcc.Graph(id='graph-3'),
                        ],
                        className='six columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        [
                            html.H4('Graph 4'),
                            dcc.Graph(id='graph-4'),
                        ],
                        className='six columns',
                        style={
                            'textAlign': 'center',
                        }
                    ),
                ],
                className='row',
                style={
                    'margin-top': '4vh'
                }
            ),

            html.Div(
                [
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='region_correlation_selection',
                                options=[
                                    {'label': 'Queensland', 'value': 'QLD1'},
                                    {'label': 'New South Wales', 'value': 'NSW1'},
                                    {'label': 'Victoria', 'value': 'VIC1'},
                                    {'label': 'South Australia', 'value': 'SA1'},
                                    {'label': 'Tasmania', 'value': 'TAS1'},
                                ],
                                value=['QLD1'],
                                multi=True
                            ),
                        ],
                        className='three columns',
                        style={
                            'textAlign': 'center',
                            'margin-left': '13vw'
                        }
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='product_correlation_selection',
                                options=[
                                    {'label': 'Futures', 'value': 'Future'},
                                    {'label': 'Caps', 'value': 'Cap'},
                                    {'label': 'Options', 'value': 'Option'}
                                ],
                                value='Future',
                                multi=False
                            ),
                        ],
                        className='two columns',
                        style={
                            'textAlign': 'center',
                            'margin-left': '35vw'
                        }
                    ),
                ],
                className='row'
            ),
        ],
        id='data-visualisation-div',
    ),

    # Forecasting page
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H3('Training data'),
                            dcc.Graph(id='training-graph'),
                        ],
                        className='six columns',
                        style={
                            'text-align': 'center'
                        }
                    ),
                    html.Div(
                        [
                            html.H3('Model controls'),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id='model-type',
                                                options=[
                                                    {'label': 'Linear regression', 'value': 'linear_regression'},
                                                    {'label': 'Ridge regression', 'value': 'ridge_regression'},
                                                    {'label': 'Lasso regression', 'value': 'lasso_regression'},
                                                    {'label': 'Elastic net regression', 'value': 'elastic_net_regression'},
                                                ],
                                                value='linear_regression',
                                                multi=False
                                            ),
                                        ],
                                        className='six columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id='forecast-target',
                                                options=[
                                                    {'label': 'Demand', 'value': 'TOTALDEMAND'},
                                                    {'label': 'Market price', 'value': 'RRP'}
                                                ],
                                                value='TOTALDEMAND',
                                                multi=False
                                            ),
                                        ],
                                        className='six columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    )
                                ],
                                className='row',
                                style={
                                    'margin-bottom': '1rem'
                                }
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id='forecast-region-selection',
                                                options=[
                                                    {'label': 'Queensland', 'value': 'QLD1'},
                                                    {'label': 'New South Wales', 'value': 'NSW1'},
                                                    {'label': 'Victoria', 'value': 'VIC1'},
                                                    {'label': 'South Australia', 'value': 'SA1'},
                                                    {'label': 'Tasmania', 'value': 'TAS1'},
                                                ],
                                                value='QLD1',
                                                multi=False
                                            ),
                                        ],
                                        className='six columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id='feature_selection',
                                                options=[
                                                    {'label': 'Date', 'value': 'SETTLEMENTDAY'},
                                                    {'label': 'Time', 'value': 'SETTLEMENTHOUR'},
                                                    {'label': 'Maximum temperature', 'value': 'MAX_TEMP'},
                                                    {'label': 'Minimum temperature', 'value': 'MIN_TEMP'},
                                                    {'label': 'Previous demand', 'value': 'TOTALDEMAND_SHIFT-1'},
                                                    {'label': 'Previous day\'s demand', 'value': 'TOTALDEMAND_ROLLING-48_SHIFT-1'},
                                                    {'label': 'Previous week\'s demand', 'value': 'TOTALDEMAND_ROLLING-336_SHIFT-1'},
                                                    {'label': 'Previous energy price', 'value': 'RRP_SHIFT-1'},
                                                    {'label': 'Previous day\'s energy price', 'value': 'RRP_ROLLING-48_SHIFT-1'},
                                                    {'label': 'Previous week\'s energy price', 'value': 'RRP_ROLLING-336_SHIFT-1'}
                                                ],
                                                value=('SETTLEMENTDAY', 'SETTLEMENTHOUR'),
                                                multi=True
                                            ),
                                        ],
                                        className='six columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    )
                                ],
                                className='row',
                                style={
                                    'margin-bottom': '1rem'
                                }
                            ),
                            html.Button(
                                'Train model',
                                id='train-button',
                                n_clicks=0,
                                style={
                                    'border-color': '#6dbf67',
                                    'color': '#6dbf67',
                                }
                            ),
                            html.H3('Feedback'),
                            html.Div(
                                [
                                    html.Div(
                                        html.H5('Train score:'),
                                        className='four columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                    html.Div(
                                        html.H5('Test score:'),
                                        className='four columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                    html.Div(
                                        html.H5('Train time:'),
                                        className='four columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                ],
                                className='row',
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        html.H5('---', id='train-loss'),
                                        className='four columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                    html.Div(
                                        html.H5('---', id='test-loss'),
                                        className='four columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                    html.Div(
                                        html.H5('--s', id='train-time'),
                                        className='four columns',
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                ],
                                className='row',
                            )
                        ],
                        className='six columns',
                        style={
                            'text-align': 'center'
                        }
                    )
                ],
                className='row'
            ),
        ],
        id='nids-div',
        style={'display': 'none'}
    ),
    html.Div(
        [
            html.Div(
                [
                    html.Img(src='https://aaas.asn.au/wp-content/uploads/2020/03/UQ-Logo.png', style={'width': '16vw'})
                ],
                className='three columns',
                style={
                    'textAlign': 'center',
                    'margin-left': '25vw'
                }
            ),
            html.Div(
                [
                    html.Img(src=app.get_asset_url('TEAM H.png'), style={'width': '16vw', 'padding-top': '4%'})
                ],
                className='three columns',
                style={
                    'textAlign': 'center'
                }
            ),
        ],
        className='row',
        style={
            'margin-top': '8vh'
        }
    )
])


@app.callback(
    Output('data-visualisation-div', 'style'),
    Output('nids-div', 'style'),
    Output('data-visualisation-toggle', 'style'),
    Output('nids-toggle', 'style'),
    Output('page-title', 'children'),
    Input('data-visualisation-toggle', 'n_clicks'),
    Input('nids-toggle', 'n_clicks')
)
def toggle_data_forecasting(data_clicks, forecasting_clicks):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        button_id = 'data-visualisation-toggle'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'data-visualisation-toggle':
        return {'display': 'block'}, {'display': 'none'}, {'background-color': '#326ba8', 'border': 'none', 'font-size': '12px', 'color': '#ffffff'}, {'font-size': '12px'}, 'Data Visualisation Dashboard'
    else:
        return {'display': 'none'}, {'display': 'block'}, {'font-size': '12px'}, {'background-color': '#326ba8', 'border': 'none', 'font-size': '12px', 'color': '#ffffff'}, 'NIDS Dashboard'


# Data visualisation callbacks
@app.callback(
    Output('graph-1', 'figure'),
    Input('feature_selection', 'value'),
    Input('nem_period_selection', 'value'),
    Input('region_selection', 'value')
)
def update_nem_graph(dependent, period, regions):
    fig = go.Figure()
    return fig


@app.callback(
    Output('graph-2', 'figure'),
    Input('product_selection', 'value'),
    Input('asx_period_selection', 'value')
)
def update_asx_graph(products, period):
    fig = go.Figure()
    return fig


@app.callback(
    Output('graph-3', 'figure'),
    Input('region_correlation_selection', 'value')
)
def update_nem_graph(regions):
    fig = go.Figure()
    return fig


@app.callback(
    Output('graph-4', 'figure'),
    Input('product_correlation_selection', 'value')
)
def update_asx_graph(product):
    return go.Figure()


if __name__ == '__main__':
    app.run_server(debug=True)
