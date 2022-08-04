import plotly.graph_objects as go
# import datetime
# import numpy as np
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash_extensions.enrich import Dash, ServersideOutput, Output, Input, Trigger
# import dask.dataframe as dd


# data = pd.read_csv('output/Stage 15 Apache.csv')
data = pd.read_csv('for_ppt.csv')
data['Timestep'] = pd.to_datetime(data['Timestep'], format='%y%m%d%H%M%S')

fig = go.Figure(data=go.Heatmap(
        z=data['SSTR'],
        x=data['Timestep'],
        y=data['DEPT'],
        colorscale='jet', 
        zmin = -10,
        zmax = 10))


fig.update_layout(
    title='Example Heatmap',
    height=800)

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
fig.update_yaxes(autorange = 'reversed')
fig.update_yaxes(exponentformat='none')

if __name__ == '__main__':
    app.run_server()