from src.data_preprocessing import load_and_merge_data
from src.feature_engineering import engineer_features
from src.model import train_model
import joblib

# Step 1: Load the data
data = load_and_merge_data()

# Step 2: Engineer features
data = engineer_features(data)

# Step 3: Train the model
model = train_model(data)

# Step 4: Save the model
joblib.dump(model, 'model.pkl')
