import pytest
from Helper_lists import *
import json
import requests

class Test_list:
    @classmethod
    def setup_class(cls):
        with open('list_data.json','r') as data:
            data=json.load(data)
        cls.key = data['key']
        cls.token = data['token']
        cls.url = data['url']
        cls.url_list=data['url_list']
        cls.name = data['uname']
        cls.testinvalidkey = data['testinvalidkey']
        cls.testinvalidtoken = data['testinvalidtoken']
        cls.testinvalidid = data['testinvalidid']
        cls.payload = {'key': cls.key, 'token': cls.token, 'name': cls.name}
        x=createboard(payload)
        print(x)
        cls.testboardid = getid('test_list')

    def teardown_method(self):
        print(deleteboard(self.testboardid))


    def test_createlist(self):#testcase_1
        gid=self.testboardid
        response=createlist(gid,'ankit')
        assert (response.status_code==200)

    def test_createlist_invalidkey(self):#testcase_2
        gid = self.testboardid
        response = createlist(gid, 'ankit',key=self.testinvalidkey,token=self.testinvalidtoken)
        assert (response.status_code == 401)


    def test_createlist_invalidid(self):#testcase_3
        gid=self.testinvalidid
        response=createlist(gid,'ankit')
        assert (response.status_code==400)



if __name__=='__main__':
    pytest.main()  