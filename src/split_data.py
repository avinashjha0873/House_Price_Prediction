import pandas as pd
from sklearn.model_selection import train_test_split
from load_data import  get_dataset
data_source_path = r"D:\Python\House_Price_Prediction\data\final\kc_house_data.csv"
train_data_path = r"D:\Python\House_Price_Prediction\data\final\split\training_house_data.csv"
test_data_path = r"D:\Python\House_Price_Prediction\data\final\split\testing_house_data.csv"

def split_data(df):
    training_data, test_data  = train_test_split(df, test_size=0.1, random_state= 7)
    print(training_data.shape)
    print(test_data.shape)
    return training_data, test_data


if __name__== "__main__":
    data = get_dataset(data_source_path)
    training_data, test_data = split_data(data)
    training_data.to_csv(train_data_path, index = False)
    test_data.to_csv(test_data_path, index=False)


