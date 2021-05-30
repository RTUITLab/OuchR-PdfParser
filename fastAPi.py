import requests
import time

time.sleep(1)
print(requests.get('http://localhost:6060/').content.decode('ascii'))
print(requests.get('http://localhost:6060/secret').content.decode('ascii'))