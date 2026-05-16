import json

def load_data():
    try:
        with open('data/workers.json', 'r') as f:
            return json.load(f)
        
    except:
        return []
    
def save_data(data):
    with open ('data/workers.json', 'w') as f:
        json.dump(data, f)
        
        
def load_bonus():
    try:
        with open('data/bonus.json', 'r') as f:
            return json.load(f)
    except:
        return[]
    
def save_bonus(data):
    with open ('data/bonus.json', 'w') as f:
        json.dump(data, f)
        
def load_fine():
    try:
        with open('data/fine.json', 'r') as f:
            return json.load(f)
    except:
        return[]
    
def save_fine(data):
    with open ('data/fine.json', 'w') as f:
        json.dump(data, f)