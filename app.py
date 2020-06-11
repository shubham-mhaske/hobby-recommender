
import dash
from dash.dependencies import  Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import tabs

from sklearn.preprocessing import Normalizer
import numpy as np
import pickle

model=pickle.load(open("pickle_SVM.pkl","rb"))

label_width = 3

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
server = app.server
#app.config.suppress_callback_exceptions = True

app.layout = html.Div(children = [

dbc.NavbarSimple(
        children=[
                
            
            
        ],
        brand="Hobby Recommender",
        
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

@app.callback(dash.dependencies.Output('results_alert','children'),
                    [dash.dependencies.Input('submit_button','n_clicks')],
                    [dash.dependencies.State('academic_olympiad','value'),
                    dash.dependencies.State('academic_scholarship','value'),
                    dash.dependencies.State('academic_school','value'),
                    dash.dependencies.State("academic_select_sub",'value'),
                    dash.dependencies.State('academic_projects','value'),
                    dash.dependencies.State('academic_grasping_power','value'),
                    dash.dependencies.State('sports_medals','value'),
                    dash.dependencies.State('sports_career','value'),
                    dash.dependencies.State('sports_activity','value'),
                    dash.dependencies.State('sports_playtime','value'),
                    dash.dependencies.State('arts_painting','value'),
                    dash.dependencies.State('arts_competition','value'),
                    dash.dependencies.State('arts_playtime','value')
                    ])
def get_results(submit_button,academic_olympiad,academic_scholarship,academic_school,academic_select_sub,academic_projects,academic_grasping_power,sports_medals,sports_career,
    sports_activity,sports_playtime,arts_painting,arts_competition,arts_playtime):

        
        input_val = [academic_olympiad,academic_scholarship,academic_school,academic_select_sub,academic_projects,sports_medals,sports_career,
                    sports_activity,arts_painting,arts_competition,academic_grasping_power,sports_playtime,arts_playtime]
        if( not input_val == [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]):
            uncat=input_val[10:13]
            Normalized= Normalizer().fit_transform(np.array(uncat).reshape(-1,1))
            features= [j for j in input_val[0:10]]
            features_encode=[]
            for z in features:
                if z==1:
                    features_encode.append(1)
                elif z==0:
                    features_encode.append(0)
                elif z=="Mathematics":
                    features_encode.append(2)
                elif z=="Science":
                    features_encode.append(3)
                elif z=="Any Language":
                    features_encode.append(0)
                elif z=="History/Geography":
                    features_encode.append(1)
            for k in Normalized :
                features_encode.append(int(k))
            prediction = model.predict(np.array(features_encode).reshape(1,-1))
            
            if int(prediction)==0:
                prediction = "Predcited Hobby : Academics "
            elif int(prediction)==1:
                prediction = "Predicted Hobby : Arts"
            elif int(prediction)==2:
                prediction = "Predicted Hobby : Sports"
            return [html.Br(),dbc.Alert(prediction,color = 'info')]
        else:
            return('No input')
        



if __name__ == "__main__":
    app.run(port = 5000)