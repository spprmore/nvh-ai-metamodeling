import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib


# Load generated structural dynamics dataset
df = pd.read_csv("data/beam_dataset.csv")


# Define input features
X = df[
    [
        "Length_m",
        "Width_m",
        "Thickness_m",
        "Youngs_Modulus_Pa",
        "Density_kg_m3",
    ]
]

# Define prediction target
y = df["Natural_Frequency_Hz"]


# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# Create Random Forest regression model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train surrogate model
model.fit(X_train, y_train)


# Predict natural frequencies for test data
y_pred = model.predict(X_test)


# Evaluate model performance / R² measures how much variation in the target is explained by the model
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("\nModel Performance")
print("-----------------")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f} Hz")

# Plot actual vs predicted natural frequencies
plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.7
)

# Ideal prediction line
min_value = min(y_test.min(), y_pred.min())
max_value = max(y_test.max(), y_pred.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--",
    color="red",
    label="Ideal Prediction"
)

plt.xlabel("Actual Natural Frequency (Hz)")
plt.ylabel("Predicted Natural Frequency (Hz)")
plt.title("Actual vs Predicted Natural Frequency")
plt.legend()
plt.grid(True)

plt.tight_layout()

# Save figure
plt.savefig(
    "figures/actual_vs_predicted.png",
    dpi=300
)

plt.close()

print("Evaluation plot saved to figures/actual_vs_predicted.png")

# Feature importance
feature_importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=True)

plt.figure(figsize=(8, 5))

feature_importance.plot(kind="barh")

plt.xlabel("Feature Importance")
plt.ylabel("Input Parameter")
plt.title("Feature Importance for Natural Frequency Prediction")

plt.tight_layout()

plt.savefig(
    "figures/feature_importance.png",
    dpi=300
)

plt.close()

print("Feature importance plot saved to figures/feature_importance.png")

# Save trained surrogate model
joblib.dump(model, "results/random_forest_model.pkl")

print("\nModel saved to results/random_forest_model.pkl")
