import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri(uri="http://127.0.0.1:5000/")

# Load data
X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Set experiment name
mlflow.set_experiment("Diabetes Regression")

# Start logging
with mlflow.start_run():
    # Parameters
    n_estimators = 95
    max_depth = 4
    
    # Model training
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Metrics
    rmse = root_mean_squared_error(y_test, predictions)

    # Log parameters and metrics
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("rmse", rmse)

    # Log model
    mlflow.sklearn.log_model(model, "model")
