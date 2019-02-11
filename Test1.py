import requests
import json

#response=requests.get("https://postman-echo.com/get?test=123")
#print(response)

#https://api.trello.com/1/boards/5c60f96c74be1b6b69fc6248?key=1dc07b278acff1d24547fa493be00901&token=4a7979afe1d507cfc6ec49ecaf54ffa888973a6955a6e4be0e733a3bb31c441b
key="1dc07b278acff1d24547fa493be00901"
token="4a7979afe1d507cfc6ec49ecaf54ffa888973a6955a6e4be0e733a3bb31c441b"
boardname="adarsh"
url="https://api.trello.com/1/boards/"
parameters={'key':key,'token':token,'name':boardname}
response2=requests.post(url,params=parameters)
#print(response2.json())
#id=response2.json()['id']
#print(id)
#getreq=requests.get("https://api.trello.com/1/boards/"+id+"?key="+key+"&token="+token+"&name="+boardname)
#print(getreq)
url_allboards="https://api.trello.com/1/members/ankitkumarpatnaik/boards/"
parameters2={'key':key,'token':token}
response3=requests.get(url_allboards,params=parameters2)
print(response3.json())
dictofnames=[]
size=len(response3.json())
print(size)
for i in range(size):#delete boards whose name start with a
    if(response3.json()[i]['name'][0]=='a'):
     dictofnames.append(response3.json()[i]['id'])
print(dictofnames)
deleteids="https://api.trello.com/1/boards/"
for i in range(len(dictofnames)):
    s=requests.delete(url+dictofnames[i]+"/",params=parameters2)
    print(s)