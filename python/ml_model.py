import pickle
from sklearn.tree import DecisionTreeClassifier
import time

# Dummy data for testing
# Format: [gateway status, dns status, network status]
data = [
    [1, 1, 1, 0],  # All okay
    [0, 1, 1, 1],  # Gateway down
    [1, 0, 1, 1],  # DNS down
    [1, 1, 0, 1]   # Network down
]

labels = [0, 1, 1, 1]  # 0 = No issue, 1 = Issue detected

def train_model():
    clf = DecisionTreeClassifier()
    clf.fit(data, labels)
    with open('model.pkl', 'wb') as model_file:
        pickle.dump(clf, model_file)
    print("Model trained and saved!")

def predict_issue(gateway_status, dns_status, network_status):
    with open('model.pkl', 'rb') as model_file:
        clf = pickle.load(model_file)
    
    result = clf.predict([[gateway_status, dns_status, network_status]])
    return result[0]

if __name__ == "__main__":
    train_model()  # Train the model first

    # Test prediction
    print("Prediction for network issue: ", predict_issue(0, 1, 1))

