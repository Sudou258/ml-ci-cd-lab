from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import pickle

X, y = load_iris(return_X_y=True)

with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

predictions = model.predict(X)
accuracy = accuracy_score(y, predictions)
print(f"Accuracy: {accuracy:.2f}")
