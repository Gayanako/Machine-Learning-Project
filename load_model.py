import pickle

# Path to your .pkl file
file_path = 'heart_disease_model.pkl'

# Reading the .pkl file
with open(file_path, 'rb') as file:  # 'rb' means read binary
    data = pickle.load(file)

# Output the data
print(data)