import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import requests
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Li-ion Cell Dashboard'),
    dcc.Dropdown(
        id='cell-dropdown',
        options=[
            {'label': 'Cell 5308', 'value': 5308},
            {'label': 'Cell 5329', 'value': 5329}
        ],
        value=5308
    ),
    html.Div([
        dcc.Graph(id='soh-pie-chart'),
        dcc.Graph(id='current-graph'),
        dcc.Graph(id='voltage-graph'),
        dcc.Graph(id='capacity-graph'),
        dcc.Graph(id='temperature-graph')
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px'})
])

@app.callback(
    [Output('soh-pie-chart', 'figure'),
     Output('current-graph', 'figure'),
     Output('voltage-graph', 'figure'),
     Output('capacity-graph', 'figure'),
     Output('temperature-graph', 'figure')],
    [Input('cell-dropdown', 'value')]
)
def update_graphs(cell_id):
    try:
        response = requests.get(f'http://localhost:8080/cell_data/{cell_id}', auth=('admin', 'password123'))
        data = response.json()

        soh = (data['discharge_capacity'] / data['nominal_capacity']) * 100

        soh_pie_chart = px.pie(values=[soh, 100-soh], names=['SoH', 'Remaining'])
        current_graph = px.line(x=data['time_data'], y=data['current_data'], title='Current vs Time')
        voltage_graph = px.line(x=data['time_data'], y=data['voltage_data'], title='Voltage vs Time')
        capacity_graph = px.line(x=data['time_data'], y=data['capacity_data'], title='Capacity vs Time')
        temperature_graph = px.line(x=data['time_data'], y=data['temperature_data'], title='Temperature vs Time')

        return soh_pie_chart, current_graph, voltage_graph, capacity_graph, temperature_graph
    except requests.RequestException as e:
        print(f"API request error: {e}")
        return [px.Figure()] * 5  # Return empty figures on error

if __name__ == '__main__':
    app.run_server(port=8081, debug=True)
