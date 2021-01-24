# import request
import json
import pprint

with open('data.json') as f:
    data = json.load(f)

# pprint.pprint(data['data'])

# print(data['data'])

def get_state_names():
    arr = []
    for x in range(len(data['data'])):
        arr.append(data['data'][x][8])
    pprint.pprint(data['data'])
    return arr

def get_state_index(name,state_list):
    return data['data'][state_list.index(name)]
