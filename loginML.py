
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def datasection():
    data = {
        "ip_region": ["UAE", "Russia", "India", "Nigeria", "USA", "China"],
        "time_hour": [13, 3, 23, 2, 14, 1],
        "failed_attempts": [0, 4, 0, 7, 0, 5],
        "label": ["legit", "suspicious", "legit", "suspicious", "legit", "suspicious"]
    }
    table = pd.DataFrame(data)
    return table

def encode_labels(table):
    global region_encoder, label_encoder
    region_encoder = LabelEncoder()
    label_encoder = LabelEncoder()
    table["ip_region_encoded"] = region_encoder.fit_transform(table["ip_region"])
    table["label_encoded"] = label_encoder.fit_transform(table["label"])
    return table

table = datasection()
table = encode_labels(table)

X = table[["ip_region_encoded", "time_hour", "failed_attempts"]]
y = table["label_encoded"]

model = DecisionTreeClassifier()
model.fit(X, y)

region_input = input("Enter  country: ")

if region_input not in region_encoder.classes_:
    print("Unknown region. Please enter one of:", list(region_encoder.classes_))
    exit()

hour_input = int(input("Enter login hour (0-23): "))
fails_input = int(input("How many failed attempts: "))

region_encoded = region_encoder.transform([region_input])[0]
new_login = [[region_encoded, hour_input, fails_input]]

prediction = model.predict(new_login)
result = label_encoder.inverse_transform(prediction)

print("This login attempt is:", result[0])
