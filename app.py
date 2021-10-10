import os
import wget
import pandas as pd
import plotly.graph_objects as go
from plotly.express import bar

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# Configure Dash app
app = dash.Dash(__name__, title='NIDS')

server = app.server

data_df = pd.read_csv(os.path.join(os.getcwd(), 'data', 'small_dataset.csv'))
data_df = pd.read_csv(os.path.join(os.getcwd(), 'data', 'NF-UNSW-NB15-v2.csv'))
data_df['id'] = data_df.index
data_df.set_index('id', inplace=True, drop=False)

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
                            html.H3('Portions of data by class'),
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
                        dcc.Dropdown(
                            id='ip-dropdown',
                            options=[
                                {'label': 'Source IPs', 'value': 'IPV4_SRC_ADDR'},
                                {'label': 'Destination IPs', 'value': 'IPV4_DST_ADDR'}
                            ],
                            value='IPV4_SRC_ADDR',
                            multi=False
                        ),
                        className='two columns offset-by-one column',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
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
                        className='two columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                    html.Div(
                        dcc.Dropdown(
                            id='pie-dropdown',
                            options=[
                                {'label': 'Different types of attacks', 'value': 'attacks'},
                                {'label': 'Benign vs malicious', 'value': 'bvm'}
                            ],
                            value='attacks',
                            multi=False,
                        ),
                        className='three columns offset-by-three columns',
                        style={
                            'textAlign': 'center'
                        }
                    ),
                ],
                className='row',
                style={'margin-left': '8px', 'margin-right': '8px'}
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.H3('Feature correlation graph'),
                            dcc.Graph(id='graph-4'),
                        ],
                        className='six columns',
                        style={
                            'textAlign': 'center',
                        }
                    ),
                    html.Div(
                        [
                            html.H3('Feature histogram by class'),
                            dcc.Graph(id='feature-histogram'),
                        ],
                        className='six columns',
                        style={
                            'textAlign': 'center'
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
                                id='correlation-dropdown',
                                options=[
                                    {'label': 'Pearson method', 'value': 'pearson'},
                                    {'label': 'Kendall method', 'value': 'kendall'},
                                    {'label': 'Spearman method', 'value': 'spearman'}
                                ],
                                value='pearson',
                                multi=False
                            ),
                        ],
                        className='two columns offset-by-two columns',
                        style={
                            'textAlign': 'center',
                            'margin-left': '17vw'
                        }
                    ),
                    html.Div(
                        [
                            dcc.Dropdown(
                                id='feature-dropdown',
                                options=[
                                    {'label': 'Source port', 'value': 'L4_SRC_PORT'},
                                    {'label': 'Destination port', 'value': 'L4_DST_PORT'},
                                    {'label': 'Protocol', 'value': 'PROTOCOL'},
                                    {'label': 'Layer 7 protocol', 'value': 'L7_PROTO'},
                                    # {'label': 'In bytes', 'value': 'IN_BYTES'},
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
                                    # {'label': 'Source to destination second bytes', 'value': 'SRC_TO_DST_SECOND_BYTES'},
                                    # {'label': 'Destination to source second bytes', 'value': 'DST_TO_SRC_SECOND_BYTES'},
                                    # {'label': 'Retransmitted in bytes', 'value': 'RETRANSMITTED_IN_BYTES'},
                                    {'label': 'Retransmitted in packets', 'value': 'RETRANSMITTED_IN_PKTS'},
                                    # {'label': 'Retransmitted out bytes', 'value': 'RETRANSMITTED_OUT_BYTES'},
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
                                    # {'label': 'DNS query type', 'value': 'DNS_QUERY_TYPE'},
                                    {'label': 'DNS TTL answer', 'value': 'DNS_TTL_ANSWER'},
                                    {'label': 'FTP command return code', 'value': 'FTP_COMMAND_RET_CODE'}
                                ],
                                value='L4_SRC_PORT',
                                multi=False
                            ),
                        ],
                        className='two columns offset-by-four columns',
                        style={
                            'textAlign': 'center',
                            'margin-left': '39vw'
                        }
                    ),
                ],
                className='row'
            ),
        ],
        id='data-visualisation-div',
    ),

    # NIDS page
    html.Div(
        [
            html.Div(
                [
                    html.H3('Model type'),
                    dcc.Dropdown(
                        id='model-dropdown',
                        options=[
                            {'label': 'Logistic Regression', 'value': 'logistic'},
                            {'label': 'Multi-layer Perceptron', 'value': 'mlp'},
                            {'label': 'Support Vector Machine', 'value': 'svm'}
                        ],
                        value='logistic',
                        className='four columns offset-by-four columns',
                        multi=False
                    )
                ],
                className='row',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '3rem'
                }
            ),
            html.Div(
                [
                    html.Div(
                        html.H4('# Malicious packets'),
                        className='two columns offset-by-two columns'
                    ),
                    html.Div(
                        html.H4('# Benign packets'),
                        className='two columns'
                    ),
                    html.Div(
                        html.H4('Total packets'),
                        className='two columns'
                    ),
                    html.Div(
                        html.H4('Accuracy'),
                        className='two columns'
                    ),
                ],
                className='row',
                style={'textAlign': 'center'}
            ),
            html.Div(
                [
                    html.Div(
                        html.H5('12042', style={'color': 'rgb(200, 30, 30'}),
                        className='two columns offset-by-two columns'
                    ),
                    html.Div(
                        html.H5('359595', style={'color': 'rgb(30, 200, 30'}),
                        className='two columns'
                    ),
                    html.Div(
                        html.H5('371637'),
                        className='two columns'
                    ),
                    html.Div(
                        html.H5('83%'),
                        className='two columns'
                    ),
                ],
                className='row',
                style={
                    'textAlign': 'center',
                    'margin-bottom': '3rem'
                }
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.H4('Significant features'),
                            dcc.Graph(id='shapley-graph'),
                        ],
                        className='five columns offset-by-one column'
                    ),
                    html.Div(
                        [
                            html.H4('Packet table'),
                            dash_table.DataTable(
                                id='packet-table',
                                columns=[
                                    {'name': 'Malicious', 'id': 'Label'},
                                    {'name': 'Source IP address', 'id': 'IPV4_SRC_ADDR'},
                                    {'name': 'Destination IP address', 'id': 'IPV4_DST_ADDR'},
                                    {'name': 'Flow duration (ms)', 'id': 'FLOW_DURATION_MILLISECONDS', 'type': 'numeric'},
                                    {'name': 'Avg. throughput src to dest', 'id': 'SRC_TO_DST_AVG_THROUGHPUT'},
                                    # {'name': 'Avg. throughput dest to src', 'id': 'DST_TO_SRC_AVG_THROUGHPUT'},
                                ],
                                data=data_df.head(n=400).to_dict('records'),
                                page_action='native',
                                page_current=0,
                                page_size=15,
                                style_cell={'textAlign': 'left'},
                                style_header={
                                    'backgroundColor': 'rgb(50, 50, 50)',
                                    'color': 'white',
                                    'fontWeight': 'bold',
                                    'textAlign': 'center'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {
                                            'filter_query': '{Label} = 0'
                                        },
                                        'backgroundColor': 'rgb(142, 232, 162)'
                                    },
                                    {
                                        'if': {
                                            'filter_query': '{Label} = 1'
                                        },
                                        'backgroundColor': 'rgb(255, 135, 135)'
                                    }
                                ]
                            )
                        ],
                        className='five columns'
                    )
                ],
                className='row',
                style={'textAlign': 'center'}
            ),
            html.Div(
                [
                    html.H4('Packet details'),
                    html.Div(
                        id='packet-details',
                        className='five columns offset-by-one column'
                    ),
                    html.Div(
                        id='packet-shapley',
                        className='five columns'
                    ),
                ],
                className='row',
                style={
                    'textAlign': 'center'
                }
            )
        ],
        id='nids-div',
        style={'display': 'none'}
    ),
    html.Div(
        [
            html.Div(
                [
                    html.Img(src='https://aaas.asn.au/wp-content/uploads/2020/03/UQ-Logo.png', style={'max-width': '16vw', 'max-height': '8vw'})
                ],
                className='three columns',
                style={
                    'textAlign': 'center',
                    'margin-left': '25vw'
                }
            ),
            html.Div(
                [
                    html.Img(src=app.get_asset_url('TEAM-H-Logo.png'), style={'max-width': '16vw', 'max-height': '8vw'})
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
def toggle_data_nids(data_clicks, nids_clicks):
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
def update_ip_graph(ip_type, class_type):
    if class_type == 'All':
        class_df = data_df
    elif class_type == 'Malicious':
        class_df = data_df.loc[data_df['Label'] == 1]
    else:
        class_df = data_df.loc[data_df['Attack'] == class_type]
    counts = class_df[ip_type].value_counts()
    return go.Figure(go.Bar(x=counts.index, y=counts.values), layout={'margin': {'t': 15}})

@app.callback(
    Output('class-pie-graph', 'figure'),
    Input('pie-dropdown', 'value')
)
def update_pie_graph(pie_type):
    if pie_type == 'bvm':
        labels = ['Benign', 'Malicious']
        counts = data_df['Label'].value_counts()
    else:
        counts = data_df['Attack'].value_counts()
        counts.drop(labels='Benign', inplace=True)
        labels = counts.index
    return go.Figure(go.Pie(labels=labels, values=counts.values), layout={'margin': {'t': 15}})


@app.callback(
    Output('feature-histogram', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_feature_histogram(feature):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data_df.loc[data_df['Label'] == 0][feature], name='Benign'))
    fig.add_trace(go.Histogram(x=data_df.loc[data_df['Label'] == 1][feature], name='Malicious'))
    fig.update_layout(
        xaxis_title=feature,
        yaxis_title='Num. packets',
        barmode='stack',
        margin={'t': 15}
    )
    return fig


@app.callback(
    Output('graph-4', 'figure'),
    Input('correlation-dropdown', 'value')
)
def update_correlation_graph(correlation):
    correlation_df = data_df.corr(method=correlation)['Label']
    correlation_df.drop(labels=['Label'], axis=0, inplace=True)
    correlation_df.sort_values(ascending=False, inplace=True)
    return go.Figure(go.Bar(x=correlation_df.index, y=correlation_df.values), layout={'margin': {'t': 15}})


@app.callback(
    Output('shapley-graph', 'figure'),
    Input('model-dropdown', 'value')
)
def update_shapley_graph(model):
    fig = go.Figure(
        bar(
            x=[0.006, -0.004, -0.008, -0.01, -0.12, 0.22, -0.3],
            y=[
                'DST_TO_SRC_SECOND_BYTES',
                'SRC_TO_DST_SECOND_BYTES',
                'TCP_WIN_MAX_IN',
                'TCP_WIN_MAX_OUT',
                'DST_TO_SRC_AVG_THROUGHPUT',
                'SRC_TO_DST_AVG_THROUGHPUT',
                'FLOW_DURATION_MILLISECONDS'
            ],
            orientation='h',
            color=[0.006, -0.004, -0.008, -0.01, -0.12, 0.22, -0.3],
            color_continuous_scale='Bluered_r'
        )
    )
    fig.update_layout(
        xaxis_title='Shapley values',
        yaxis_title='Features',
        height=520,
        margin={
            't': 0,
            'b': 0,
            'l': 10,
            'r': 10
        }
    )
    return fig


@app.callback(
    Output('packet-details', 'children'),
    Input('packet-table', 'active_cell')
)
def update_shapley_graph(active_cell):
    if active_cell:
        row = data_df.loc[active_cell['row_id']]
        row_df = row.to_frame()
        row_df['FEATURES'] = row_df.index
        table = dash_table.DataTable(
            data=row_df.to_dict('records'),
            columns=[
                {'name': 'Features', 'id': 'FEATURES'},
                {'name': 'Values', 'id': str(active_cell['row_id'])}
            ],
            page_action='native',
            page_current=0,
            page_size=15,
            style_cell={'textAlign': 'left'},
            style_header={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'fontWeight': 'bold',
                'textAlign': 'center'
            }
        )
        return table
    else:
        return 'Select a cell from the table above and the details will appear here'


if __name__ == '__main__':
    app.run_server(debug=True)
