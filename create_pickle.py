import pickle

data = {
    "name": "John",
    "age": 25,
    "skills": ["Python", "ML"]
}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

print("Pickle file created successfully!")
