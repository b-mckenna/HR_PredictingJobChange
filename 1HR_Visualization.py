import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("/Users/brendanmckenna/Dropbox/Projects/HR_DataScientists_JobChange/Data/aug_train.csv")
data.info()
data.isnull().sum()

# One-off Visualizations
## Gender (matplotlib)
gender = data['gender'].value_counts("Female").plot(kind='pie')
plt.show()

## Education Level (plotly express)
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go

el = data['education_level'].value_counts()

fig = px.pie(
    el, 
    names=el.index, 
    values='education_level', 
    title='Education Level', 
    width=800,
    height=500 
)
fig.update_traces(textinfo='label+percent').show()

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
fig.update_traces(hoverinfo='value', textinfo='label+percent').show()

# Prints variable count + percentage and creates a circle graph to illustrate
def cat_summary(dataframe, col_name, plot=False):
    df = pd.DataFrame(
        {col_name:data[col_name].value_counts(), "Ratio": 100* data[col_name].value_counts() / len(data)})
    print(df)
    
    if plot:
        plt.figure(figsize=(7,5))
        plt.pie (df["Ratio"], labels=df.index, labeldistance=1.15, wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' }, autopct = "%1.1f%%", pctdistance=0.85, textprops={'fontsize': 10})
            
        #draw circle
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.show()
        print("="*50)

col_name = data.columns
graph_cols = [col for col in data.columns if data[col].nunique() < 40]

for col in graph_cols:
    cat_summary (data, col, plot=True)

# which variables have the highest number of individuals interested in a job change
def target_summary(dataframe, target, plot=False):
    df = pd.DataFrame({"TARGET_MEAN": dataframe[target].mean(),
                        "TARGET_MEDIAN": dataframe[target].median(),
                        "COUNT": dataframe[target].count()})
    print(df)
    if plot==True:
        sns.barplot(x=df.index, y=df["TARGET_MEAN"])
        plt.xticks(rotation=45)
        plt.xlabel(df.index.name.upper())
        plt.show();
        print("="*50)

cats = [col for col in data.columns if (data[col].nunique() < 20)]

for col in cats:
    target_summary(data, "target", plot=True)