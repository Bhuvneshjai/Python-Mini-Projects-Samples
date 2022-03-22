# Problem Statement:
# The task you have to perform is “Pickling Iris.”
# For this, Check the UC Irvine Machine Learning Repository site to get the dataset.
# You can search the Iris dataset through their searchable interface. Follow the following steps to download the dataset:
# Go to https://archive.ics.uci.edu/ml/index.php
# On Most Popular Data Sets, you will see the name “Iris.”
# Open the Iris dataset.
# Click on the Data folder. A new tab will open, which contains some files.
# Click on the Iris. data file to download the text file.

import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
print(data)

l1 = data.split("\n")
print(l1)

l2 = [item.split(",") for item in l1 if len(item)!=0]
print(l2)

with open("myiris.pkl","wb") as f:
    pickle.dump(l2,f)

# To read this pickle file you can use this code
# with open("myiris.pkl","rb") as f:
#     print(pickle.load(f))