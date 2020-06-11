import dash
from dash.dependencies import  Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

label_width = 3 


academic_tab = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Participated in Olympiad ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'academic_olympiad'
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Got Scholarship ?"),
                    width = label_width
                
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'academic_scholarship'
                    )
                )
            ]),

            dbc.Row([
                dbc.Col(
                    dbc.Alert("Love going to School ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'academic_school'
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Favourite Subject ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                       dbc.Select( 
                            id="academic_select_sub",
                            options=[
                                {"label": "Mathematics", "value": "Mathematics"},
                                {"label": "Science", "value": "Science"},
                                {"label": "Any Language", "value": "Any Language"},
                                {"label": "History/Geography", "value": "History/Geography"},
                            ],
                            value = 99
                            
                        )
                    )
                
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Done projects ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        inline = True,
                        value = 99,
                        id = 'academic_projects'
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Grasping power ?"),
                    width = label_width
                ),
                dbc.Col(
                    dcc.Slider(
                        min=1,
                        max = 5,
                        step =1,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5'
                        },
                        id = 'academic_grasping_power',
                        value = 99
                    )
                )
            ]),
        ]
    ),
    className="mt-3",
)

 
sports_tab = dbc.Card(
    dbc.CardBody(
        [
             dbc.Row([
                dbc.Col(
                    dbc.Alert("Medals Won ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'sports_medals'
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Career in sports ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'sports_career'
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Activity in Sports ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'sports_activity'
                    )
                )   
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Playtime for Sports ?"),
                    width = label_width
                ),
                dbc.Col(
                    dcc.Slider(
                        min=1,
                        max = 5,
                        step =1,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5'
                        },
                        id = 'sports_playtime',
                        value = 99
                    )
                )
            ]),
        ]
    ),
    className="mt-3",
)


arts_tab = dbc.Card(
    dbc.CardBody(
        [
             dbc.Row([
                dbc.Col(
                    dbc.Alert("Create fantasy paintings ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'arts_painting'
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Won art competitions ?"),
                    width = label_width
                ),
                dbc.Col(
                    
                        dbc.RadioItems(
                        options=[
                            {"label": "Yes", "value": 1},
                            {"label": "No", "value": 0},
                        ],
                        value = 99,
                        inline = True,
                        id = 'arts_competition'
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Alert("Playtime for Arts ?"),
                    width = label_width
                ),
                dbc.Col(
                    dcc.Slider(
                        min=1,
                        max = 5,
                        step = 1,
                        marks={
                            1: '1',
                            2: '2',
                            3: '3',
                            4: '4',
                            5: '5'
                        },
                        value = 99,
                        id = 'arts_playtime'
                    )
                )
            ])
        ]
    ),
    className="mt-3",
)


result_tab =dbc.Card(
    dbc.CardBody([
        dbc.Button("Get Results",id = 'submit_button'),
        html.Div(id = 'results_alert')
    ])
)












