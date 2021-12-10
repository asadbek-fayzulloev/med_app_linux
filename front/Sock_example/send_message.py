import requests
r = requests.get('http://192.168.92.196:8888/index.php/user/list?limit=20')
print(r.json())