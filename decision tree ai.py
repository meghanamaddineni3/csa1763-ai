import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# Sample data for demonstration
data = {
    'Feature1': [1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    'Feature2': [0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    'Label': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and Labels
X = df[['Feature1', 'Feature2']]  # Features
y = df['Label']  # Labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = clf.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')

# Visualize the Decision Tree
plt.figure(figsize=(10, 6))
plot_tree(clf, feature_names=X.columns, class_names=np.unique(y), filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# Print the rules of the decision tree
tree_rules = export_text(clf, feature_names=list(X.columns))
print("\nDecision Tree Rules:")
print(tree_rules)
