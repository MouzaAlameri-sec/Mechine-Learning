__Author__ = "Mouza Alameri"
__Date__ = "27/05/2025"

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class DemandPredictor:
    def __init__(self):
        self.df = None
        self.model = LinearRegression()
    
    def generate_data(self, samples=100):
        marketing = np.random.uniform(1000, 5000, samples)
        temperature = np.random.uniform(10, 35, samples)
        noise = np.random.normal(0, 500, samples)
        demand = 0.4 * marketing + 1.8 * temperature + noise
        self.df = pd.DataFrame({
            'MarketingSpend': marketing,
            'Temperature': temperature,
            'Demand': demand
        })

    def train(self):
        X = self.df[['MarketingSpend', 'Temperature']]
        y = self.df['Demand']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Model trained. MSE: {mse:.2f}")

    def predict(self, marketing_spend, temperature):
        input_df = pd.DataFrame([[marketing_spend, temperature]], columns=['MarketingSpend', 'Temperature'])
        prediction = self.model.predict(input_df)[0]
        print(f"Predicted Demand: {prediction:.2f}")
        return prediction

if __name__ == "__main__":
    predictor = DemandPredictor()
    predictor.generate_data()
    predictor.train()
    predictor.predict(marketing_spend=3500, temperature=22)
