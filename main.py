import requests
import requests as rq

base_url = 'http://www.boredapi.com/api/activity/'

payload = {'participents':1}

request = rq.get(base_url,params=payload)
data = request.json()

print('Responses:',data)
print('---')
print('Activity:',data['activity'])
print('Type:',data['type'])