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
            ##### Mild violence
            """
        ),
        dcc.RadioItems(
            id='mild_violence_input',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            value=1
        ),  
        dcc.Markdown(
            """
            ##### Simulated gambling
            """
        ),
        dcc.RadioItems(
            id='gambling_input',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            value=1
        ),
        dcc.Markdown(
            """
            ##### No descriptor
            """
        ),
        dcc.RadioItems(
            id='no_descriptor_input',
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
        ),
        dcc.Markdown(
            """
            ##### Suggestive themes
            """
        ),
        dcc.RadioItems(
            id='theme_input',
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
        dcc.Markdown(
            """
            ##### Violence
            """
        ),
        dcc.RadioItems(
            id='violence_input',
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
        )
    ],
    md=4
)

column3 = dbc.Col(
    [
        dcc.Markdown('',id='prediction-content', style={
        'textAlign':'center',
        'font-size':30})
        # dcc.Graph(id='shap-content')   
    ]
)

@app.callback(
    Output('prediction-content','children')
    # Output('shap-content','figure')
    [ Input('mild_violence_input', 'value'),
      Input('gambling_input', 'value'),
      Input('no_descriptor_input', 'value'),
      Input('language_input', 'value'),
      Input('theme_input', 'value'),
      Input('violence_input', 'value'),
      Input('blood_and_gore_input', 'value'),
      Input('fantasy_violence_input', 'value'),
      Input('strong_language_input', 'value'),
      Input('blood_input', 'value')
     ])


def predict(mild_violence,simulated_gambling,no_descriptors,language,suggestive_themes,
violence,blood_and_gore,fantasy_violence,strong_language,blood):
    df = pd.DataFrame(columns=['mild_violence',
                                'simulated_gambling',
                                'no_descriptors',
                                'language',
                                'suggestive_themes',
                                'violence',
                                'blood_and_gore',
                                'fantasy_violence',
                                'strong_language',
                                'blood'], 
    data=[[mild_violence,simulated_gambling,no_descriptors,language,suggestive_themes,
    violence,blood_and_gore,fantasy_violence,strong_language,blood]])
    y_pred = pipeline.predict(df)[0]
    # explainer = shap.TreeExplainer(pipeline)
    # shap_values = explainer.shap_values(df)
    # shap_plot = shap.summary_plot(shap_values[0], df)
    return "The ESRB rating is {}".format(y_pred)
    # return "The ESRB rating is {}".format(y_pred), shap_plot

layout = dbc.Row([column1,column2,column3])