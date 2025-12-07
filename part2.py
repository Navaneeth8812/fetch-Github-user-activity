import requests
from pprint import pprint
user_name = input("enter your user name")
url = f"https://api.github.com/users/{user_name}"
user_data= requests.get(url).json()
pprint(user_data)


