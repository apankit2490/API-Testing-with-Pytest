import requests
import json

with open('list_data.json', 'r') as data:
    data = json.load(data)
key = data['key']
token = data['token']
url = data['url']
url_list = data['url_list']
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
        if i['fullName'].lower()==nameofuser.lower():
            return i['id']

def addmembertoboard(id,fullname,email,type,key=key,token=token):
    url_add=url+id+'/members'
    response=requests.put(url_add,params={'key':key,'token':token,'id':id,'fullName':fullname,'email':email,'type':type})
    return response
def createlist(boardid,nameoflist,key=key,token=token):
    response=requests.post(url_list,params={'idBoard':boardid,'name':nameoflist,'key':key,'token':token})
    return response
def getlistid(id,listname):
    response = requests.get(url + id +'/lists', params=payload)
    for i in response.json():
        if i['name'].lower() == listname.lower():
            return i['id']
def createcard(listid,name):
    url = "https://api.trello.com/1/cards"

    querystring = {"idList": listid, "keepFromSource": "all",'key':key,'token':token}

    response = requests.request("POST", url, params=querystring)

# createboard(payload)
# id=getid('test_list')
# createlist(id,'ankit')
# lid=getlistid(id,'ankit')
# print(lid)
# createcard(lid,'ankitcard')

#print(getid('test_fobidden'))
# while(True):
#     id=getid('test_BOARD')
#     deleteboard(id)
# print(addmembertoboard('5c615ba7f5c7564b8f9e8c43','ankit','ankitkumarpatnaik001@gmail.com','normal'))
# print(getmemberid('5c615ba7f5c7564b8f9e8c43','ankit'))

if __name__=='__main__':
   dd='x'