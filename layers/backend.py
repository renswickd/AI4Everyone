import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv(r"C:\Users\RENS\Desktop\resume_update\model-deployment\FastAPI\data\Social_Network_Ads.csv")
print(data.columns)
print(data.head())

#get user input for dependent variable and junk variables
y_var = input("Enter the dependent variable: ").strip()
junk_vars = input("Enter the junk variables(comma separated): ").strip().split(',')
scale_method = input("Enter the Scaling Method (S/M): ").strip().upper()[0]

#clean dataset after user input
x_cols = [col for col in data.columns if col not in junk_vars]
x_cols.remove(y_var)
print(x_cols)

object_cols = [i for i in data[x_cols].columns if data[i].dtypes == object]
numeric_cols = [i for i in data[x_cols].columns if data[i].dtypes != object]

if scale_method == "S":
    object = StandardScaler()
elif scale_method == "M":
    object = MinMaxScaler()

data_numeric = pd.DataFrame(object.fit_transform(data[numeric_cols]),columns=numeric_cols)
print(data_numeric.head())

data_object = pd.get_dummies(data[object_cols],drop_first=True)
print(data_object.head())

data_modified = pd.concat([data_numeric,data_object],axis=1)
#if y variable is object then apply LabelEncoder else leave as it is
#data_modified['y_var'] = data[y_var]######## to apply label encoder

print(data_modified.head())