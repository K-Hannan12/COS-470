from sklearn.model_selection import train_test_split
import pandas as pd

# Get test data
data = pd.read_csv('HW5/homework5_data.csv')

# Split data randomly 15% test 85% traning
traning_data,test_data = train_test_split(data,train_size=0.85, test_size= 0.15, random_state=42)

# Split data by Year 
year_traning_data = data[~data['YEAR'].isin([2010, 2015])]
year_test_data =  data[data['YEAR'].isin([2010, 2015])]

# Convert to csv file
traning_data.to_csv('HW5/traning_data_persent.csv',index = False)
year_traning_data.to_csv('HW5/traning_data_year.csv',index = False)
test_data.to_csv('HW5/test_data_persent.csv',index = False)
year_test_data.to_csv('HW5/test_data_year.csv',index = False)
