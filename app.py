import pandas as pd
import plotly.graph_objects as go
from os.path import dirname, abspath

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# Configure Dash app
app = dash.Dash(__name__, title='NIDS')

# Load in data
data_df = pd.read_csv(dirname(abspath(__file__)) + '/data/NF-UNSW-NB15-v2.csv')

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
                            html.H3('Potions of data by class'),
                            dcc.Graph(id='class-pie-graph'),
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
                                id='ip-dropdown',
                                options=[
                                    {'label': 'Source IPs', 'value': 'IPV4_SRC_ADDR'},
                                    {'label': 'Destination IPs', 'value': 'IPV4_DST_ADDR'}
                                ],
                                value='IPV4_SRC_ADDR',
                                multi=False
                            ),
                        ],
                        className='three columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='class-dropdown',
                                options=[
                                    {'label': 'All packets', 'value': 'All'},
                                    {'label': 'Benign packets', 'value': 'Benign'},
                                    {'label': 'Malicious packets', 'value': 'Malicious'},
                                    {'label': 'Exploits', 'value': 'Exploits'},
                                    {'label': 'Generic', 'value': 'Generic'},
                                    {'label': 'Fuzzers', 'value': 'Fuzzers'},
                                    {'label': 'Reconnaissance', 'value': 'Exploits'},
                                    {'label': 'DoS', 'value': 'Exploits'},
                                    {'label': 'Analysis', 'value': 'Exploits'},
                                    {'label': 'Backdoor', 'value': 'Exploits'},
                                    {'label': 'Shellcode', 'value': 'Exploits'},
                                    {'label': 'Worms', 'value': 'Exploits'}
                                ],
                                value='All',
                                multi=False
                            ),
                        ],
                        className='three columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='pie-dropdown',
                                options=[
                                    {'label': 'Benign vs malicious', 'value': 'bvm'},
                                    {'label': 'Different types of attacks', 'value': 'attacks'},
                                ],
                                value='attacks',
                                multi=False,
                            ),
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
                            html.H4('Feature histogram'),
                            dcc.Graph(id='feature-histogram'),
                        ],
                        className='six columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        [
                            html.H4('Feature comparison plot'),
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
                                id='feature-dropdown',
                                options=[
                                    {'label': 'Source port', 'value': 'L4_SRC_PORT'},
                                    {'label': 'Destination port', 'value': 'L4_DST_PORT'},
                                    {'label': 'Protocol', 'value': 'PROTOCOL'},
                                    {'label': 'Layer 7 protocol', 'value': 'L7_PROTO'},
                                    {'label': 'In bytes', 'value': 'IN_BYTES'},
                                    {'label': 'In packets', 'value': 'IN_PKTS'},
                                    {'label': 'Out bytes', 'value': 'OUT_BYTES'},
                                    {'label': 'Out packets', 'value': 'OUT_PKTS'},
                                    {'label': 'TCP flags', 'value': 'TCP_FLAGS'},
                                    {'label': 'Client TCP flags', 'value': 'CLIENT_TCP_FLAGS'},
                                    {'label': 'Server TCP flags', 'value': 'SERVER_TCP_FLAGS'},
                                    {'label': 'Flow duration', 'value': 'FLOW_DURATION_MILLISECONDS'},
                                    {'label': 'Duration in', 'value': 'DURATION_IN'},
                                    {'label': 'Duration out', 'value': 'DURATION_OUT'},
                                    {'label': 'Minimum TTL', 'value': 'MIN_TTL'},
                                    {'label': 'Maximum TTL', 'value': 'MAX_TTL'},
                                    {'label': 'Longest flow packet', 'value': 'LONGEST_FLOW_PKT'},
                                    {'label': 'Shortest flow packet', 'value': 'SHORTEST_FLOW_PKT'},
                                    {'label': 'Minimum packet length', 'value': 'MIN_IP_PKT_LEN'},
                                    {'label': 'Maximum packet length', 'value': 'MAX_IP_PKT_LEN'},
                                    {'label': 'Source to destination second bytes', 'value': 'SRC_TO_DST_SECOND_BYTES'},
                                    {'label': 'Destination to source second bytes', 'value': 'DST_TO_SRC_SECOND_BYTES'},
                                    {'label': 'Retransmitted in bytes', 'value': 'RETRANSMITTED_IN_BYTES'},
                                    {'label': 'Retransmitted in packets', 'value': 'RETRANSMITTED_IN_PKTS'},
                                    {'label': 'Retransmitted out bytes', 'value': 'RETRANSMITTED_OUT_BYTES'},
                                    {'label': 'Retransmitted out packets', 'value': 'RETRANSMITTED_OUT_PKTS'},
                                    {'label': 'Source to destination average throughput', 'value': 'SRC_TO_DST_AVG_THROUGHPUT'},
                                    {'label': 'Destination to source average throughput', 'value': 'DST_TO_SRC_AVG_THROUGHPUT'},
                                    {'label': 'Number of packets < 128 bytes', 'value': 'NUM_PKTS_UP_TO_128_BYTES'},
                                    {'label': 'Number of packets from 128 to 256 bytes', 'value': 'NUM_PKTS_128_TO_256_BYTES'},
                                    {'label': 'Number of packets from 256 to 512 bytes', 'value': 'NUM_PKTS_256_TO_512_BYTES'},
                                    {'label': 'Number of packets from 512 to 1024 bytes', 'value': 'NUM_PKTS_512_TO_1024_BYTES'},
                                    {'label': 'Number of packets from 1024 to 1514 bytes', 'value': 'NUM_PKTS_1024_TO_1514_BYTES'},
                                    {'label': 'TCP window maximum in', 'value': 'TCP_WIN_MAX_IN'},
                                    {'label': 'TCP window maximum out', 'value': 'TCP_WIN_MAX_OUT'},
                                    {'label': 'ICMP type', 'value': 'ICMP_TYPE'},
                                    {'label': 'ICMP IPV4 type', 'value': 'ICMP_IPV4_TYPE'},
                                    {'label': 'DNS query ID', 'value': 'DNS_QUERY_ID'},
                                    {'label': 'DNS query type', 'value': 'DNS_QUERY_TYPE'},
                                    {'label': 'DNS TTL answer', 'value': 'DNS_TTL_ANSWER'},
                                    {'label': 'FTP command return code', 'value': 'FTP_COMMAND_RET_CODE'}
                                ],
                                value='L4_SRC_PORT',
                                multi=False
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
    Input('ip-dropdown', 'value'),
    Input('class-dropdown', 'value')
)
def update_nem_graph(ip_type, class_type):
    if class_type == 'All':
        class_df = data_df
    elif class_type == 'Malicious':
        class_df = data_df.loc[data_df['Label'] == 1]
    else:
        class_df = data_df.loc[data_df['Attack'] == class_type]
    counts = class_df[ip_type].value_counts()
    return go.Figure([go.Bar(x=counts.index, y=counts.values)])

@app.callback(
    Output('class-pie-graph', 'figure'),
    Input('pie-dropdown', 'value')
)
def update_nem_graph(pie_type):
    if pie_type == 'bvm':
        labels = ['Benign', 'Malicious']
        counts = data_df['Label'].value_counts()
    else:
        counts = data_df['Attack'].value_counts()
        counts.drop(labels='Benign', inplace=True)
        labels = counts.index
    return go.Figure(go.Pie(labels=labels, values=counts.values))


@app.callback(
    Output('feature-histogram', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_nem_graph(feature):
    return go.Figure([go.Histogram(x=data_df[feature])])


@app.callback(
    Output('graph-4', 'figure'),
    Input('product_correlation_selection', 'value')
)
def update_asx_graph(product):
    return go.Figure()


if __name__ == '__main__':
    app.run_server(debug=True)
