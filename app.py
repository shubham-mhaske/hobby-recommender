import dash
from dash.dependencies import  Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import tabs

#from sklearn.preprocessing import Normalizer
import numpy as np
import pickle

#model=pickle.load(open("pickle_SVM.pkl","rb"))

label_width = 3

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
server = app.server

app.layout = html.Div(children = [

dbc.NavbarSimple(
        children=[
                
            
            
        ],
        brand="Hobby Recommender",
        brand_href="#",
        color="primary",
        dark = True
        
    ),
    html.Br(),
    dbc.Container([
        dbc.Tabs([
            dbc.Tab(tabs.academic_tab,label = 'Academic'),
            dbc.Tab(tabs.sports_tab,label = 'Sports'),
            dbc.Tab(tabs.arts_tab,label = 'Arts'),
            dbc.Tab(tabs.result_tab,label = 'Results')
        ])
        
    ]),
    html.Footer(dbc.Row(dbc.Alert("Made with ❤️ by FE Comp",color = 'secondary'),justify = 'center'))
])



if __name__ == "__main__":
    app.run(port = 5000)
