# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import shap

# Imports from this application
from app import app
from joblib import load
import pandas as pd
pipeline = load('pages/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
        dcc.Markdown(
            """
            ##### Blood
            """
        ),
        dcc.RadioItems(
            id='blood_input',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            value=1
        ),  
        dcc.Markdown(
            """
            ##### Fantasy violence
            """
        ),
        dcc.RadioItems(
            id='fantasy_violence_input',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            value=1
        ),  
        dcc.Markdown(
            """
            ##### Blood and Gore
            """
        ),
        dcc.RadioItems(
            id='blood_and_gore_input',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            value=1
        ),  
        dcc.Markdown(
            """
            ##### Strong Language
            """
        ),
        dcc.RadioItems(
            id='strong_language_input',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            value=1
        ),  
        dcc.Markdown(
            """
            ##### Language
            """
        ),
        dcc.RadioItems(
            id='language_input',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            value=1
        )   
 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('',id='prediction-content', style={
        'textAlign':'center',
        'font-size':30}),
        # dcc.Graph(id='shap-content')   
    ]
)

@app.callback(
    Output('prediction-content','children'),
    # Output('shap-content','figure')
    [ Input('blood_input', 'value'),
      Input('fantasy_violence_input', 'value'),
      Input('blood_and_gore_input', 'value'),
      Input('strong_language_input', 'value'),
      Input('language_input', 'value')
     ])


def predict(blood, fantasy_violence, blood_and_gore, strong_language,language):
    df = pd.DataFrame(columns=['blood', 'fantasy_violence', 'blood_and_gore', 'strong_language', 'language'], 
    data=[[blood, fantasy_violence, blood_and_gore, strong_language,language]])
    y_pred = pipeline.predict(df)[0]
    # explainer = shap.TreeExplainer(pipeline)
    # shap_values = explainer.shap_values(df)
    # shap_plot = shap.summary_plot(shap_values[0], df)
    return "The ESRB rating is {}".format(y_pred)
    # return "The ESRB rating is {}".format(y_pred), shap_plot

layout = dbc.Row([column1,column2])