"""
This file includes all analysis done on the variables. These functions should be testing correlations and finding patterns. 
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO fix bug in target_summary. when creating a dataframe it wants data to have an index. 

# Showing the variables with the most people interested in a job change
def target_summary(data, target, plot=False):
    df = pd.DataFrame({"TARGET_MEAN": data[target].mean(),
                        "TARGET_MEDIAN": data[target].median(),
                        "COUNT": data[target].count()})
    print(df)
    if plot==True:
        sns.barplot(x=df.index, y=df["TARGET_MEAN"])
        plt.xticks(rotation=45)
        plt.xlabel(df.index.name.upper())
        print("="*50)
        return plt.show();
        

# Displays variable count and percentage
def cat_summary(data, col_name, plot=False):
    df = pd.DataFrame(
        {col_name:data[col_name].value_counts(), "Ratio": 100* data[col_name].value_counts() / len(data)})
    print(df)
    
    if plot:
        plt.figure(figsize=(7,5))
        plt.pie (df["Ratio"], labels=df.index, labeldistance=1.15, wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' }, autopct = "%1.1f%%", pctdistance=0.85, textprops={'fontsize': 10})
            
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        print("="*50)
        return plt.show()
        

