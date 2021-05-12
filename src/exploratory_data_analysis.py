import pandas as pd
from load_data import get_dataset
from data_wrangling import change_data_type
training_data_path = r"D:\Python\House_Price_Prediction\data\processed\cleaned_training_house_data.csv"
zipcode_data_path = r"D:\Python\House_Price_Prediction\data\processed\zipcode_house_data.csv"
final_data_path = r"D:\Python\House_Price_Prediction\data\final\kc_house_data.csv"

def feature_engineering(data):
    data['Age'] = 2020 - data['Year_Built']
    data['Change_In_Sqft_Living'] = data['Sqft_Living_2015'] - data['Sqft_Living']
    data['Change_In_Sqft_Plot'] = data['Sqft_Plot_2015'] - data['Sqft_Plot']
    data = data.drop(['Year_Built', 'Year_Renovated','Transaction_Date'], axis = 1)
    return data


def add_ratios(data):
    Housing_Data_New = data
    Housing_Data_New['sqft_living_zipcode_ratio'] = Housing_Data_New.Sqft_Living / Housing_Data_New.ZipCode_Total_sqft_living
    Housing_Data_New['sqft_lot_zipcode_ratio'] = Housing_Data_New.Sqft_Plot / Housing_Data_New.ZipCode_Total_sqft_lot
    Housing_Data_New['sqft_above_zipcode_ratio'] = Housing_Data_New.Sqft_Above / Housing_Data_New.ZipCode_Total_sqft_above
    Housing_Data_New['sqft_basement_zipcode_ratio'] = Housing_Data_New.Sqft_Basement / Housing_Data_New.ZipCode_Total_sqft_basement
    Housing_Data_New['sqft_living15_zipcode_ratio'] = Housing_Data_New.Sqft_Living_2015 / Housing_Data_New.ZipCode_Total_sqft_living15
    Housing_Data_New['sqft_lot15_zipcode_ratio'] = Housing_Data_New.Sqft_Plot_2015 / Housing_Data_New.ZipCode_Total_sqft_lot15
    Housing_Data_New['sqft_median_price_zipcode_ratio'] = Housing_Data_New.Price / Housing_Data_New.Zipcode_Median_housePrice
    Housing_Data_New.drop(columns=['ZipCode_Total_sqft_living', 'ZipCode_Total_sqft_lot', 'ZipCode_Total_sqft_above', 'ZipCode_Total_sqft_basement', 'ZipCode_Total_sqft_living15', 'ZipCode_Total_sqft_lot15'], inplace = True)
    return Housing_Data_New

if __name__ ==    "__main__":
    data = get_dataset(training_data_path)
    data = change_data_type(data)
    data = feature_engineering(data)
    zipcode_data = get_dataset(zipcode_data_path)
    Housing_data = data.merge(zipcode_data, how= 'left', on='Zipcode')
    Housing_data = add_ratios(Housing_data)
    Housing_data.to_csv(final_data_path, index = False)
    print(Housing_data.info())
