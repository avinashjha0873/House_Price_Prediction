import pandas as pd
original_path = r"D:\Python\House_Price_Prediction\given_data\kc_house_data.csv"
data_source_path = r"D:\Python\House_Price_Prediction\data\raw\kc_house_data.csv"
data = pd.read_csv(original_path)
data.to_csv(data_source_path)
