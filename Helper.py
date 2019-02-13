import requests
import json

with open('data.json', 'r') as data:
    data = json.load(data)
key = data['key']
token = data['token']
url = data['url']
name = data['uname']
payload = {'key': key, 'token': token, 'name': name}
allboardsurl=data['allboardsurl']


def createboard(payload=payload):
    response = requests.post(url, params=payload)
    return response
def deleteboard(id):
    response=requests.delete(url+id,params=payload)
    return response
def getid(boardname):
    response=requests.get(allboardsurl,params=payload)
    for i in response.json():
        if i['name']==boardname:
            return i['id']
def getmemberid(id,nameofuser):
    response=requests.get(url+id+'/members',params=payload)
    for i in response.json():
        if i['fullName']==nameofuser:
            return i['id']

def addmembertoboard(id,fullname,email,type):
    url_add=url+id+'/members'
    parameter = payload
    print(parameter)
    response=requests.put(url_add,params={'key':key,'token':token,'id':id,'fullName':fullname,'email':email,'type':type})
    return response


#print(getid('test_fobidden'))
# id=getid('test_BOARD')
# deleteboard(id)
print(addmembertoboard('5c615ba7f5c7564b8f9e8c43','ankit','ankitkumarpatnaik001@gmail.com','normal'))
print(getmemberid('5c615ba7f5c7564b8f9e8c43','ankit'))