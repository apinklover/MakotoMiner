import requests
from requests.structures import CaseInsensitiveDict
import random
import time

time.sleep(5)

url = "http://3.139.237.81/makotocoin"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
num_hashes = 0

for i in range(49200000, 50000001):
    data = '{ "input": ' + str(i) + ' }'
    resp = requests.post(url, headers=headers, data=data)
    num_hashes += 1
    print("Hash #" + str(num_hashes), data, resp)
    if "200" in resp:
        print("Correctly guessed the hash\nHash was " + data)
        break

input("Press ENTER to exit.")
