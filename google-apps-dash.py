# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# 读取处理过的google-play-store-apps.csv
df = pd.read_csv("1.csv")
# 第一个散点图
fig = px.scatter(df, x="Reviews", y="Rating",
                 size="Installs",color="Category",hover_name="App",
                 log_x=False, size_max=55)

fig.update_layout(
    title='Rating VS Review per App',
    margin=dict(t=70, b=40),
    paper_bgcolor='rgb(248, 248, 255)',
    #plot_bgcolor='rgb(248, 248, 255)',
)

# 第二个旭日图
fig1 = px.sunburst(df,
                   path=['Type', 'Content Rating','Category'],
                   color='Content Rating',
                   values='Installs')

fig1.update_layout(
    title='Proportion of Price Type & Categories per Content Rating',
    margin=dict(l=0, r=10, t=70, b=40),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
)

# 第三个图含两个子图：条状图和折线图
y_num = [262, 262, 288, 294, 294, 300, 710, 897, 1582]
y_num_percentage = [3.23, 3.23, 3.55, 3.63, 3.63, 3.70, 8.76, 11.07, 19.52]
y_reviews_avg = [18347, 182394, 75885, 171569, 60141, 555262, 51538, 141398, 525411]
x = ['PHOTOGRAPHY', 'BUSINESS', 'MEDICAL', 'PERSONALIZATION', 'LIFESTYLE', 'FINANCE', 'TOOLS', 'GAME', 'FAMILY']

# Creating two subplots
fig2 = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                    shared_yaxes=False, vertical_spacing=0.001)

fig2.append_trace(go.Bar(
    x=y_num_percentage,
    y=x,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Proportion of the Top Nine Categories of Apps',
    orientation='h',
), 1, 1)

fig2.append_trace(go.Scatter(
    x=y_reviews_avg, y=x,
    mode='lines+markers',
    line_color='rgb(128, 0, 128)',
    name='Average Review for each Category, per App',
), 1, 2)

fig2.update_layout(
    title='Proportion & average review for top nine categories of apps',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    yaxis2=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
        domain=[0, 0.85],
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.42],
    ),
    xaxis2=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0.47, 1],
        side='top',
        dtick=25000,
    ),
    legend=dict(x=0.029, y=1.038, font_size=10),
    margin=dict(l=100, r=20, t=70, b=40),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
)

annotations = []

y_s = np.round(y_num_percentage, decimals=2)
y_nw = np.rint(y_reviews_avg)

# Adding labels
for ydn, yd, xd in zip(y_nw, y_s, x):
    # labeling the scatter average review
    annotations.append(dict(xref='x2', yref='y2',
                            y=xd, x=ydn - 20000,
                            text='{:,}'.format(ydn),
                            font=dict(family='Arial', size=12,
                                      color='rgb(128, 0, 128)'),
                            showarrow=True))
    # labeling the bar proportion
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd + 3,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=12,
                                      color='rgb(50, 171, 96)'),
                            showarrow=False))

fig2.update_layout(annotations=annotations)

app.layout = html.Div([
    html.Div([
        html.H3(children='Data Visualization (Google-Play-Store-Apps) ——— Jasmine Ding (HCI LAB 3)'),
    ],
    style={'padding': '5px','text-align':'center','box-shadow':'#666 0px 0px 2px','margin-bottom':'5px','background-image':'url("/assets/1.jpg")'}),
    html.Div([
        dcc.Graph(
            id='Rating-vs-Reviews',
            figure=fig
        )
    ],
    style={'width': '59%', 'display': 'inline-block', 'margin-right': '1%'}),
    html.Div([
        dcc.Graph(
            id='Price-vs-Content Rating',
            figure=fig1
        ),
    ],
    style={'width': '40%', 'display': 'inline-block'}),
        dcc.Graph(
            id='Content Rating-vs-Number&Reviews',
            figure=fig2
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)
