import joblib
import pandas as pd
from preprocess import load_data

model = joblib.load("model/linear_regression_model_with_ma.pkl")

df = load_data("data/feders_weight_with_moving_averages.xlsx")

X = df[["Feeder1_Percent","Feeder2_Percent","Feeder3_Percent"]]

predictions = model.predict(X)

df["Prediction"] = predictions

df.to_excel("results/prediction_results.xlsx", index=False)

print("Predictions saved")
