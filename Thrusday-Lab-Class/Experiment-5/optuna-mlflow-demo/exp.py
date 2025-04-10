from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split

import optuna
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the objective function for hyperparameter optimization
def objective(trial):
    # Start a new MLflow run for each trial
    with mlflow.start_run():
        # Hyperparameter search space
        n_estimators = trial.suggest_int("n_estimators", 50, 200)  # Number of trees
        max_depth = trial.suggest_int("max_depth", 3, 20)  # Maximum depth of trees

        # Initialize the RandomForest model with selected hyperparameters
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)

        # Train the model
        model.fit(X_train, y_train)

        # Predict and calculate accuracy
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Log the hyperparameters and the accuracy with MLflow
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("accuracy", accuracy)

        return accuracy

if __name__ == "__main__":
    # Start MLflow experiment
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000/")
    mlflow.set_experiment("Iris-RandomForest-Hyperparameter-Tuning")  # Set an experiment name if necessary

    # Create an Optuna study to optimize the objective function
    study = optuna.create_study(direction="maximize")  # We want to maximize accuracy
    study.optimize(objective, n_trials=50)  # Run 50 trials

    # Best trial information
    print(f"Best Trial: {study.best_trial.params}")
    print(f"Best Accuracy: {study.best_value}")
