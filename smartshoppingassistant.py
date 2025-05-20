__Author__ = "Mouza Alameri"
__Data__ = "20/05/2025"

from sklearn.tree import DecisionTreeClassifier
import pandas as pd

class SmartShoppingAssistant:
    def __init__(self):
        self.model = None
        self.train_model()

    def train_model(self):
        data = {
            "luxury_items": [1, 4, 0, 2, 5, 3],
            "total_spend": [100, 1000, 50, 200, 1500, 300],
            "visits_per_month": [5, 15, 2, 6, 18, 10],
            "segment": ["Saver", "Premium", "Saver", "Saver", "Premium", "Impulsive"]
        }
        df = pd.DataFrame(data)
        X = df[["luxury_items", "total_spend", "visits_per_month"]]
        y = df["segment"]
        self.model = DecisionTreeClassifier()
        self.model.fit(X, y)

    def expert_label(self, luxury_items):
        return "High Spender 💸" if luxury_items > 3 else "Regular Shopper 🛍️"

    def predict(self, luxury_items, total_spend, visits_per_month):
        expert = self.expert_label(luxury_items)
        user_data = [[luxury_items, total_spend, visits_per_month]]
        ml_result = self.model.predict(user_data)[0]
        return expert, ml_result

assistant = SmartShoppingAssistant()

print("Answer the following:")
lux = int(input("Luxury items: "))
spend = float(input("Total spend: "))
visits = int(input("Visits/month: "))

expert_result, ml_result = assistant.predict(lux, spend, visits)

print("\n--- Smart Shopper Analysis ---")
print(f" Expert Opinion: {expert_result}")
print(f" ML Prediction: You are likely a '{ml_result}' shopper.")
