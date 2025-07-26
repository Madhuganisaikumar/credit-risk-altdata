from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(data):
    X = data.drop(columns=['id', 'default'])
    y = data['default']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    print("Classification Report:\n")
    print(classification_report(y_test, y_pred))
    
    return clf
