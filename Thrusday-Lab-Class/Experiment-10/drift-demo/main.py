import pandas as pd
from sklearn.datasets import load_iris
from evidently import Report
from evidently.presets import DataDriftPreset
import matplotlib.pyplot as plt


# Load base dataset
iris = load_iris()
df_ref = pd.DataFrame(iris.data, columns=iris.feature_names)

# Simulate drift by changing feature distributions
df_drift = df_ref.copy()
df_drift["sepal length (cm)"] += 1.5  # Simulate shift
df_drift["sepal width (cm)"] *= 1.2  # Simulate scale change

# Create Evidently report
report = Report(metrics=[DataDriftPreset()])
eval = report.run(reference_data=df_ref, current_data=df_drift)

# Save as HTML report
eval.save_html("iris_drift_report.html")
print("Drift report saved as iris_drift_report.html")
