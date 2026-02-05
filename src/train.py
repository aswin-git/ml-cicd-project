import pandas as pd
import joblib
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("data/iris.csv")
data = data.drop('Id', axis=1)
X = data.drop("Species", axis=1)
y = data["Species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

version = int(time.time())
model_path = f"artifacts/model_v{version}.pkl"

joblib.dump(model, model_path)

X_test.to_csv("artifacts/X_test.csv", index=False)
y_test.to_csv("artifacts/y_test.csv", index=False)

with open("artifacts/latest.txt", "w") as f:
    f.write(str(version))

print(f"Model trained and saved at {model_path}")
