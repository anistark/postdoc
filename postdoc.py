import requests
import config

postman_url = config.postman_url

r = requests.get(postman_url)
postman_data = r.json()

print('Name:', postman_data['name'])
print('Total Folders:', len(postman_data['folders']))
print('Total Requests:', len(postman_data['requests']))

# Generate docs in markdown
