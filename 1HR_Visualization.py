import pandas as pd
import matplotlib.pyplot as plt


# Load data
data = pd.read_csv("/Users/brendanmckenna/Dropbox/Projects/HR_DataScientists_JobChange/Data/aug_train.csv")
# Reviewing the data
data.info()
data.isnull().sum()
data.describe()
data.head()

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

# Displays variable count and percentage
def cat_summary(dataframe, col_name, plot=False):
    df = pd.DataFrame(
        {col_name:data[col_name].value_counts(), "Ratio": 100* data[col_name].value_counts() / len(data)})
    print(df)
    
    if plot:
        plt.figure(figsize=(7,5))
        plt.pie (df["Ratio"], labels=df.index, labeldistance=1.15, wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' }, autopct = "%1.1f%%", pctdistance=0.85, textprops={'fontsize': 10})
            
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.show()
        print("="*50)

col_name = data.columns
graph_cols = [col for col in data.columns if data[col].nunique() < 40]

for col in graph_cols:
    cat_summary (data, col, plot=True)

# Showing the variables with the most people interested in a job change
cats = [col for col in data.columns if (data[col].nunique() < 20)]
for col in cats:
    Analysis.target_summary(data, "target", plot=True)