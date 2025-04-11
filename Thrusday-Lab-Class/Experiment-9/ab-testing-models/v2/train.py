from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib

X, y = load_iris(return_X_y=True)
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

joblib.dump(model, './model_v2.pkl')
print("✅ Model B saved as model_v2.pkl")
