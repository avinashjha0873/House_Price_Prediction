import json

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
from load_data import get_dataset
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score
import math
from data_wrangling import change_data_type
import joblib

train_data_path = r"D:\Python\House_Price_Prediction\data\final\split\training_house_data.csv"
score_file_path = r"D:\Python\House_Price_Prediction\reports\scores.json"
param_file_path = r"D:\Python\House_Price_Prediction\reports\params.json"

def evaluate(actual, pred):
    r2 = r2_score(actual, pred)
    mse = mean_squared_error(actual, pred)
    rmse = math.sqrt(mse)
    mae = mean_absolute_error(actual, pred)
    results = {
        'r2_score': r2,
        'root_mean_square_error' : rmse,
        'mean_abosolute_error' : mae

    }
    return results

def train_and_evaluate(data):
    data['Id'] = data['Id'].astype('object')
    data['Zipcode'] = data['Zipcode'].astype('object')
    train_X, test_X, train_y, test_y = train_test_split(
                                                data.drop(columns = ['Price']),
                                                data.Price,
                                                test_size = 0.1,
                                                random_state = 7
                                            )
    print(train_X.info())
    model = LinearRegression()
    model.fit(train_X, train_y)
    y_tr_pred = model.predict(train_X)
    y_te_pred = model.predict(test_X)

    results = evaluate(test_y, y_te_pred)

    print("R-Squared value for Training Data: ", r2_score(train_y, y_tr_pred))
    print("Mean Absolute Error for Training Data: ", mean_absolute_error(train_y, y_tr_pred))
    print("Mean Square Error for Training Data: ", mean_squared_error(train_y, y_tr_pred))

    with open(score_file_path, 'w') as f:
        scores = results
        json.dump(scores, f, indent=4)

    model_path = r"D:\Python\House_Price_Prediction\models\model.joblib"
    joblib.dump(model, model_path)

if __name__=="__main__":
    train_data = get_dataset(train_data_path)
    train_and_evaluate(train_data)
