import pytest
import json
import requests
class Test_board_push:
    @classmethod
    def setup_class(cls):
        with open('data.json','r') as data:
            data=json.load(data)
        cls.key=data['key']
        cls.token=data['token']
        cls.url=data['url']
        cls.name=data['uname']
        cls.payload={'key':cls.key,'token':cls.token,'name':cls.name}

    '''def test_newboard(self):#TestCase_1
        response=requests.post(self.url,params=self.payload)
        assert (response.status_code==200)
        board_id=response.json()['id']
        response=requests.get(self.url+'/'+board_id,params=self.payload)
        assert (response.json()['id']==board_id)'''
    def test_newboard_invalid_keyortoken(self):#TestCase_2
        response=requests.post(self.url,params={'key':'','token':''})
        assert (response.status_code==401)
    def test_newboard_inavlid_name(self):#TestCase_3
        response = requests.post(self.url,params={'key':self.key,'token':self.token,'name':None})
        print(self.payload)
        assert (response.status_code == 400)
    def test_newboard_forbidden(self):





if __name__=='__main__':
    pytest.main()