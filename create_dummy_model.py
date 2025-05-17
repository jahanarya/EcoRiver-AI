import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np

# Dummy data
X = np.array([[0, 0], [1, 1]])
y = np.array([0, 1])

# Simple logistic regression model train kora
model = LogisticRegression()
model.fit(X, y)

# Model save kora
with open('encroachment_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Dummy model saved as encroachment_model.pkl")
