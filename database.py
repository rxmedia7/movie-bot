import json

def load_db():
    try:
        with open("database.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_db(db):
    with open("database.json", "w") as f:
        json.dump(db, f, indent=4)