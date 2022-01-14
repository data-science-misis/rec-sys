#!/usr/bin/env python
# encoding: utf-8
import os

import dash
from dash import dash_table
from dash import html
import json

from dash import dcc, Output, Input
from flask import request, jsonify
import prediction_engine
from data_provider import database

port = int(os.environ.get("PORT", 5000))

app = dash.Dash(__name__)
server = app.server


app.layout = html.Div([
    html.H1("Wine Recommender"),

    html.H3("Please pick a user"),
    dcc.Dropdown(
        id='user-dropdown',
        options=[{'label': user, 'value': user} for user in prediction_engine.get_user_ids()] + [
            {'label': 'Unknown', 'value': 'Unknown'}],
        value='Unknown'
    ),
    html.Div(id='user-output-container'),

    html.H2("Recommendations"),
    html.Div(id='recommendations-datatable'),

    html.H2("Dataset"),
    dash_table.DataTable(
        id='datatable-row-ids',
        columns=[
            {'name': i, 'id': i, 'deletable': False, 'selectable': True} for i in database().columns
            # omit the id column
            if i != 'id'
        ],
        data=database().to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=False,
        selected_rows=[],
        page_action='native',
        page_current=0,
        page_size=10,
    ),
    html.Div(id='datatable-interactivity-container'),
])


@app.callback(
    Output('recommendations-datatable', 'children'),
    Input('user-dropdown', 'value')
)
def update_output(value, k=10):
    user_id = value if value != 'Unknown' else None
    method, predictions = predict(user_id, k)

    table = html.H6("No recommendations generated") if predictions.empty else dash_table.DataTable(
            columns=[
                {'name': i, 'id': i, 'deletable': False, 'selectable': True} for i in predictions.columns
                # omit the id column
                if i != 'id'
            ],
            data=predictions.to_dict('records'),
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode='multi',
            row_selectable='multi',
            row_deletable=False,
            selected_rows=[],
            page_action='native',
            page_current=0,
            page_size=10,
        )

    return [
        html.H2(method),
        table
    ]


@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    Input('datatable-interactivity', 'selected_columns')
)
def update_styles(selected_columns):
    return [{
        'if': {'column_id': i},
        'background_color': '#D2F3FF'
    } for i in selected_columns]


@server.route("/health", methods=['GET'])
def hello():
    return "<p>Service is up and running</p>"


def predictions_to_response(prediction_type, predictions):
    return json.dumps(
        {
            'type': prediction_type,
            'predictions': predictions,
        }
    )


@server.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(prediction_engine.get_user_ids())


@server.route('/api/predictions', methods=['POST'])
def controller_predict():
    record = json.loads(request.data)
    user_id = record.get('user_id')
    k = record.get('predictions_count')

    method, predictions = predict(user_id, k)

    return predictions_to_response(method, predictions.to_dict(orient='records'))


def predict(user_id=None, k=None):
    if not user_id:
        return 'popularity based', prediction_engine.predict_popular(k)
    else:
        return 'collaborative-filtering', prediction_engine.predict_collaborative_filtering(user_id)


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=port)
