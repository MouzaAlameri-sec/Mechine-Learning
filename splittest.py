
__Author__ : "Mouza Alameri"
__Date__ : "26/05/2025"

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Step 1: Made-up data
data = {
    'login_attempts': [1, 2, 10, 3, 50, 60, 1, 5, 100, 2],
    'username_length': [6, 8, 5, 9, 3, 2, 7, 6, 2, 8],
    'used_common_password': [0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    'is_attack': [0, 0, 1, 0, 1, 1, 0, 0, 1, 0]  # 0 = normal, 1 = attack
}

df = pd.DataFrame(data)
print(df)

# Step 2: Define input (X) and output (y)
input_data = df[['login_attempts', 'username_length', 'used_common_password']]
output_data = df['is_attack']

# Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    input_data, output_data, test_size=0.2, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Step 4: Train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Step 5: Predict on test set
y_pred = clf.predict(X_test)

# Step 6: Evaluation
print("\nEvaluation Report:")
print(classification_report(y_test, y_pred))





