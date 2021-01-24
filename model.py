import request
import json

with open('data.json') as f:
    data = json.load(f)
print(data['data'][0][0])
print("HELLO")
f.close()
