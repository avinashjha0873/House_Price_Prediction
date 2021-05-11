import pandas as pd
from load_data import get_dataset

training_data_path = r"D:\Python\House_Price_Prediction\data\raw\kc_house_data.csv"
cleaned_data_path = r"D:\Python\House_Price_Prediction\data\processed\cleaned_training_house_data.csv"
zipcode_data_path = r"D:\Python\House_Price_Prediction\data\processed\zipcode_house_data.csv"

def change_data_type(data):
    data['Id'] = data['Id'].astype('object')
    data['Transaction_Date'] = pd.to_datetime(data['Transaction_Date'])
    data['Zipcode'] = data['Zipcode'].astype('object')
    return data

def drop_rows(df):
    data = df.drop_duplicates(['Id'], keep='last')
    data = data[~(data.Bedroom_Count == 33)]
    Housing_data = data[~((data.Bathroom_Count == 0) | (data.Bedroom_Count == 0))]
    Housing_data.loc['Plot_Living'] = Housing_data['Sqft_Plot'] - Housing_data['Sqft_Living']
    Housing_data.loc['Plot-Living_2015'] = Housing_data['Sqft_Plot_2015'] - Housing_data['Sqft_Living_2015']
    Housing_Data = Housing_data[~(Housing_data.duplicated(['Latitude', 'Longitude', 'Year_Built','Transaction_Date', 'Sqft_Living', 'Sqft_Plot'], keep = False))]
    return Housing_data

def add_zipcode_summary(data):
    zipcode = data.groupby('Zipcode').agg(
        Listing_per_Zip_Code = pd.NamedAgg(column = 'Id', aggfunc = 'count'),
        ZipCode_Total_sqft_living = pd.NamedAgg(column = 'Sqft_Living', aggfunc = 'sum'),
        ZipCode_Total_sqft_lot = pd.NamedAgg(column = 'Sqft_Plot', aggfunc = 'sum'),
        ZipCode_Total_sqft_above = pd.NamedAgg(column = 'Sqft_Above', aggfunc = 'sum'),
        ZipCode_Total_sqft_basement = pd.NamedAgg(column = 'Sqft_Basement', aggfunc = 'sum'),
        ZipCode_Total_sqft_living15 = pd.NamedAgg(column = 'Sqft_Living_2015', aggfunc = 'sum'),
        ZipCode_Total_sqft_lot15 = pd.NamedAgg(column = 'Sqft_Plot_2015', aggfunc = 'sum'),
        Zipcode_Median_housePrice = pd.NamedAgg(column = 'Price', aggfunc = 'median')
    ).reset_index()
    return zipcode


if __name__ ==    "__main__":
    data = get_dataset(training_data_path)
    data = change_data_type(data)
    data = drop_rows(data)
    data.to_csv(cleaned_data_path, index = False)
    zipcode_data  = add_zipcode_summary(data)
    zipcode_data.to_csv(zipcode_data_path, index = False)



