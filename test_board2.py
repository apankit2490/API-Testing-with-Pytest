import pytest
import json
import requests
class Test_board_push2:
    @classmethod
    def setup_class(cls):
        with open('data.json','r') as data:
            data=json.load(data)
            cls.key = data['key']
            cls.token = data['token']
            cls.url = data['url']
            cls.name = data['uname']
            cls.payload = {'key': cls.key, 'token': cls.token, 'name': cls.name}
    def test_update_board(self):#testcase_41
        id="5c610bdaef382018a436b32e"
        response=requests.put(self.url+id,params={'key':self.key,'token':self.token,'name':'divya hg'})
        assert (response.status_code==200)
        name=requests.get(self.url+'/'+id,params=self.payload).json()['name']
        assert (name=='divya hg')
    def test_update_board_INVALID_KEY(self):#testcase_41
        id="5c610bdaef382018a436b32e"
        response=requests.put(self.url+id,params={'key':'dscs','token':self.token,'name':'divya hg'})
        assert (response.status_code==401)


