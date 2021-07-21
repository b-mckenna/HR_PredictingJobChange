from Visualization import *
from Analysis import *
from Loader import *

class Main:
    def __init__(self):
        self
    
if __name__ == '__main__':
    my_app = Main()
    datapath = "/Users/brendanmckenna/Dropbox/Projects/HR_DataScientists_JobChange/Data/aug_train.csv"
    data = load(datapath)
    data.info()
    data.isnull().sum()
    data.describe()
    data.head()

    # Visualize some of the variables
    visualize_gender
    visualize_education(data)
    visualize_experience(data)

    # Analyze the variables
    col_name = data.columns

    graph_cols = [col for col in data.columns if data[col].nunique() < 40]
    for col in graph_cols:
        cat_summary (data, col, plot=True)

    # Showing the variables with the most people interested in a job change
    cats = [col for col in data.columns if (data[col].nunique() < 20)]
    for col in cats:
        target_summary(data, "target", plot=True)