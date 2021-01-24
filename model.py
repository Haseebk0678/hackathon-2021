# import request
import json
import pprint

with open('data.json') as f:
    data = json.load(f)


pprint.pprint(data['data'])
