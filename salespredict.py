
__Author__ = "Mouza Alameri" 
__Date__ = "19/05/2025"

import pandas as pd   #imports tables 
from sklearn.preprocessing import LabelEncoder #to turn yes/no values into 0/1
from sklearn.tree import DecisionTreeClassifier #ML model  tree of rules 

def table(): 
    data = {
    "visit_time": [2,12,5,20,1,15],
    "pages_seen": [1,5,2,10,1,8],
    "adz_clicked": ["no","yes","no","yes","no","yes"],
    "purrchase": ["no","yes","no","yes","no","yes"]
}

table = pd.DataFrame(data)

table()

def dataencoder():
    le = LabelEncoder
    table["adz_clicked_encoded"] = le.fit_transform(table["adz_clicked"])
    table["purrchase_encoded"] = le.fit_transform(table["purrchase"])

dataencoder()

def trainmodel():
    input = table[["visit_time","pages_seen","adz_encoded"]] #visit time and pages are already numbers no need to encode 
    output = table[["purrchase_encoded"]]
    
    model = DecisionTreeClassifier
    model.fit(input,output)
    
trainmodel()

def makepred(): 
    new_visit = [[10,6,1]]
    pred = model.predict(new_visit)
    
    print("purchase predicition:", "yes" if pred[0] ==1 else "No")
    
makepred()
