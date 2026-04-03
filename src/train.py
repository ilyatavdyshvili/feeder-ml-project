import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from preprocess import load_data

df = load_data("data/feders_weight_with_moving_averages.xlsx")

X = df[["Feeder1_Percent","Feeder2_Percent","Feeder3_Percent"]]
y = df["Weight_t_h"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model/linear_regression_model_with_ma.pkl")

print("Model trained and saved")
