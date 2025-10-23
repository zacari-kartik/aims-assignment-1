import pandas as pd
import numy as np

data = pd.read_csv(data.csv)
df = pd.DataFrame(data)
print(df)
print("\nMissing values count=")
print(df.isnull().sum())

#imputation with mean
def impute_with_mean(dataframe, column_name):
  mean_value = dataframe[column_name].mean()
  dataframe[column_name].fillna(value=mean_value, inplace=true)
  return dataframe

#imputation with median
def impute_with_median(dataframe, column_name):
  median_value  =  dataframe[column_name].median()
  dataframe[column_name].fillna(value=median_value, inplace=true)
  return dataframe

#imputation with mode
def impute_with_mode(dataframe, column_name):
  mode_value = dataframe[column_name].mode()
  return dataframe
