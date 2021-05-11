import pandas as pd
import os
import argparse
original_path = r"D:\Python\House_Price_Prediction\given_data\kc_house_data.csv"
data_source_path = r"D:\Python\House_Price_Prediction\data\raw\kc_house_data.csv"


def get_dataset(path):
    data = pd.read_csv(path)
    return data

def save_dataset(data, path):
    Column_Names = ['Id', 'Transaction_Date','Price', 'Bedroom_Count', 'Bathroom_Count',
                    'Sqft_Living', 'Sqft_Plot', 'Floor_Count', 'Waterfront', 'View',
                    'Condition', 'Grade', 'Sqft_Above', 'Sqft_Basement', 'Year_Built',
                    'Year_Renovated', 'Zipcode', 'Latitude', 'Longitude', 'Sqft_Living_2015', 'Sqft_Plot_2015']
    data.columns = Column_Names
    print(data.shape)
    data.to_csv(path, index= False)


if __name__ == "__main__":
    df = get_dataset(original_path)
    save_dataset(df, data_source_path)