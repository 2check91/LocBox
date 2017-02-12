import json

data = {}
data['users'] = []
data['users'].append({
    'phone': '7325527269',
    'auth_time': '2016-02-12T21:24:20',
    'trans_open': False
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
