# --------------------------------------------------------------
# Sustainable Agriculture Prediction using Decision Tree (With Input)
# --------------------------------------------------------------

from sklearn.tree import DecisionTreeClassifier

# --------------------------------------------------------------
# 1. Training Data (Sample – you can replace with real dataset)
# --------------------------------------------------------------

# Features:
# Policy Support, Soil Health, Subsidies, Training, Water Scheme
X = [
    [70, 85, 1, 1, 1],
    [30, 35, 0, 0, 0],
    [50, 60, 1, 1, 1],
    [80, 90, 1, 1, 1],
    [20, 25, 0, 0, 0],
    [10, 15, 0, 0, 0],
    [90, 95, 1, 1, 1],
    [40, 45, 0, 1, 1],
    [55, 70, 1, 1, 1],
    [25, 30, 0, 0, 0],
]

# Labels: 1 = Sustainable, 0 = Unsustainable
y = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# --------------------------------------------------------------
# 2. Train the Decision Tree Model
# --------------------------------------------------------------

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# --------------------------------------------------------------
# 3. Take Input From User
# --------------------------------------------------------------

print("\nEnter values to check sustainability:\n")

policy = int(input("Enter Policy Support Index (0–100): "))
soil = int(input("Enter Soil Health Score (0–100): "))
subs = int(input("Subsidies Available? (1=Yes, 0=No): "))
train = int(input("Training Available? (1=Yes, 0=No): "))
water = int(input("Water Scheme Support? (1=Yes, 0=No): "))

user_data = [[policy, soil, subs, train, water]]

# --------------------------------------------------------------
# 4. Predict
# --------------------------------------------------------------

prediction = model.predict(user_data)

if prediction[0] == 1:
    print("\n🌱 RESULT: The region is **SUSTAINABLE** ✔")
else:
    print("\n⚠ RESULT: The region is **UNSUSTAINABLE** ✖")
