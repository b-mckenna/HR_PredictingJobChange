import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
"""
This file includes all visualizations for the app. Each function takes in a dataframe.
"""
from plotly.subplots import make_subplots
import plotly.graph_objs as go

def visualize_gender(data):
    ## Gender (matplotlib)
    gender = data['gender'].value_counts("Female").plot(kind='pie')
    return plt.show()

def visualize_education(data):
    ## Education Level (plotly express)
    el = data['education_level'].value_counts()
    fig = px.pie(
        el, 
        names=el.index, 
        values='education_level', 
        title='Education Level', 
        width=800,
        height=500 
    )
    return fig.update_traces(textinfo='label+percent').show()

def visualize_experience(data):
    ## Experience (plotly express)
    ex = data.value_counts('experience')
    ex.columns = ['Years', 'People']
    ex.name = 'Experience'

    fig = px.pie(
        ex,
        names=ex.index,
        values=ex,
        title='Experience_level', 
        width=800,
        height=500 
    )
    return fig.update_traces(hoverinfo='value', textinfo='label+percent').show()