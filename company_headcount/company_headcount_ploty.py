# import dash
# from dash.dependencies import Input, Output
# import dash_core_components as dcc
# import dash_html_components as html
#
# import pandas as pd
# from datetime import datetime as dt
# # import chart_studio.plotly as py
# # import chart_studio.graph_objes as go
#
#
# from parse_data import Data
#
#
# class FindPlotData:
#     def __init__(self):
#         self.db = Data('companies_headcount.db')
#
#     def get_labels_from_db(self):
#         results = self.db.fetchall('select * from companies')
#         for result in results:
#             print(result)
#             result['label'] = result.pop('id')
#             result['value'] = result.pop('company')
#             result['label'] = result['value']
#
#         return results
#
#     # def get_data_from_db(self):
#     #     db =
#     #     df = pd.read_sql_query('select * from headcount where company = "target"')
#     #     py.iplot([go.Bar(x=df.month, y=df.headcount)])
#
#     def update_dropdown_options(values):
#         if len(values) == 5:
#             return [option for option in dropdown_options if OPTIONS["value"] in values]
#         else:
#             return OPTIONS
#
#
# f = FindPlotData()
# dropdown_options = f.get_labels_from_db()
# f.get_labels_from_db()
#
#
#
#
# app = dash.Dash('Company Headcount',
#                 external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
#
#
# app.layout = html.Div([
#     dcc.Dropdown(
#         id='company',
#         options=dropdown_options,
#         multi=True
#     ),
#
#     dcc.Graph(id='my-graph')
# ], style={'width': '500'})
#
#
#
#
#
# @app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
# def update_graph(selected_dropdown_value):
#     return {
#         'data': [{
#             'x': 1,
#             'y': 2
#         }],
#         'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
#     }
#
#
# OPTIONS = []
#
# @app.callback(
#     Output(component_id="company", component_property="options"),
#     [
#         Input(component_id="company", component_property="value"),
#     ],
# )
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     app.run_server()
