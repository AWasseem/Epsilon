import dash
from dash import html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import os


dash.register_page(__name__, name="Exploration")

file_path = os.path.join(
    os.getcwd(),
    "GitHubProjects",
    "Mid Project",
    "Dash",
    "Train_cleaned.csv",
)

df = pd.read_csv(file_path)



tab1 = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(dcc.Graph(figure=px.imshow(df.corr(numeric_only=True),text_auto=True,aspect="auto",title="Correlation Matrix"))),
                        dbc.Row(dbc.Label("there is no strong relation ship between data except new generated earning column showing strong relation with wage_per_hour and this is a normal relation."))
                    ],
                    width=12,
                ),
            ]
        )
    ],
    fluid=True,
)
tab2 =dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [                        
                        dbc.Row(dcc.Graph(figure=px.histogram(data_frame=df[["gender","income_above_limit"]],x="gender",facet_col="income_above_limit",barmode="group"))),
                        dbc.Row(dbc.Label("It is clear that the majority of the population earns less than $50,000; with a higher number of females falling into the lower income bracket."))
                    ],
                    width=12,
                ),
            ]
        )
    ],
    fluid=True,
)
tab3 =dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [                        
                        dbc.Row(dcc.Graph(figure=px.pie(data_frame=round(df[df["earning"]>0].groupby("education_level")["earning"].mean().reset_index(),2), names="education_level", values="earning"))),
                        dbc.Row(dbc.Label("the university education came the first in earning compared to other education"))
                    ],
                    width=12,
                ),
            ]
        )
    ],
    fluid=True,
)
tab4 =dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [                        
                        dbc.Row(dcc.Graph(figure=px.histogram(data_frame=df.education_level.value_counts().reset_index(),x="education_level",y="count",title="Earning by Education Level"))),
                        
                    ],
                    width=12,
                ),
            ]
        )
    ],
    fluid=True,
)
tab5 =dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [    
                      dbc.Row(dcc.Graph(figure=px.histogram(data_frame=df[["race","earning"]],x="race", y="earning", histfunc="avg"))),
                       
                    ],
                    width=12,
                ),
            ]
        )
    ],
    fluid=True,
)
tab6 =dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [    
                        dcc.Dropdown(placeholder="Select a Age", options=sorted(df.age.unique()),className="form-select",id="ddlColumns1",multi=True ),                    
                        dbc.Row(dcc.Graph(figure={},id="ShowGraph1"))
                       
                    ],
                    width=12,
                ),
            ]
        )
    ],
    fluid=True,
)
layout = dbc.Container(
    [
        dbc.Tabs(
            [
                dbc.Tab(tab1, label="Corelation Exploration"),
                dbc.Tab(tab2, label="Comparison of males and females earning over $50,000?"),
                dbc.Tab(tab3, label="Comparison between education level average earning?"),
                dbc.Tab(tab4, label="University education completion compared to other education?"),
                dbc.Tab(tab5, label="Race earning comparison?"),
                dbc.Tab(tab6, label="Race earning by Age?"),
            ]
        ),
    ]
)

@callback(
    Output(component_id="ShowGraph1", component_property="figure"),
    Input(component_id="ddlColumns1", component_property="value"),
)
def update_graph(value_chosen):
    
    if value_chosen is not None:
        fig = px.histogram(data_frame=df[["race","earning","age"]][df["age"].isin(value_chosen)],x="race", y="earning",color="age",barmode="group", histfunc="avg")
        return fig