import requests
import json

pwdstore = "http://104.236.66.171:8080/pwd"

a = 'gerry'
b = 'uber'
c = 'makerBot67'

def get_pwd(usr, key):
	get_response = requests.get(url=pwdstore+"?usr="+usr+"&key="+key)
	return get_response.text
	
def save_pwd(usr, key, pwd):
	post_data = {"usr":usr,"pwd":pwd, "key":key}
	headers = {'content-type': 'application/json'}
	post_response = requests.post(url=pwdstore, data=json.dumps(post_data),headers=headers)
	if post_response == 201:
		return "success"
	else:
		return "failed"

	
