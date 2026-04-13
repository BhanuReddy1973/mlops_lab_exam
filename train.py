import json
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
import pickle

def train_model():

    
    print("Name: Bhanu Reddy")
    print("Registration Number: 2022bcd0026")

    
    # Load dataset
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predict and calculate MSE
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"Model MSE: {mse:.4f}")
    
    # Save model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Save metrics
    metrics = {
        "mse": float(mse),
        "name": "Bhanu Reddy",
        "register": "2022bcd0026"
    }
    
    with open('metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print("Model and metrics saved successfully!")
    return mse

if __name__ == "__main__":
    train_model()
