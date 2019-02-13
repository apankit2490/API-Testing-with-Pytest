import pytest
from Helper_boards import *
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
        cls.testinvalidkey = data['testinvalidkey']
        cls.testinvalidtoken = data['testinvalidtoken']
        cls.testinvalidid = data['testinvalidid']
        cls.payload = {'key': cls.key, 'token': cls.token, 'name': cls.name}
        createboard(payload)
        cls.testboardid = getid('test_BOARD')
        cls.forbidden_id = data['forbidden_id']
    def teardown_class(self):
        print(deleteboard(self.testboardid))

    def test_update_board(self):#testcase_41
        id=self.testboardid
        response=requests.put(self.url+id,params={'key':self.key,'token':self.token,'name':'divya hg'})
        assert (response.status_code==200)
        name=requests.get(self.url+'/'+id,params=self.payload).json()['name']
        assert (name=='divya hg')

    def test_update_board_INVALID_KEY(self):#testcase_42
        id=self.testboardid
        response=requests.put(self.url+id,params={'key':self.testinvalidkey,'token':self.testinvalidtoken,'name':'divya hg'})
        assert (response.status_code==401)

    def test_update_board_INVALID_boardid(self):  # testcase_43
        id = self.testinvalidid
        response = requests.put(self.url + id, params={'key': self.key, 'token': self.token, 'name': 'divya hg'})
        assert (response.status_code == 400)

    def test_update_board_forbidden(self):#testcase_44
        id=self.forbidden_id#another's board
        response=requests.put(self.url+id,params={'key':self.key,'token':self.token,'name':'divya hg'})
        assert (response.status_code==401)

    def test_update_boardmember(self):#testcase_45
        id = self.testboardid
        addmember = addmembertoboard(id, 'divya', 'divya.hgreddy@gmail.com', 'normal')
        assert (addmember.status_code==200)

    def test_update_boardmember_invalidkey(self):  # testcase_46
        id = self.testboardid
        response = addmembertoboard(id,'divya', 'divya.hgreddy@gmail.com', 'normal',self.testinvalidkey,self.testinvalidtoken)
        assert (response.status_code == 401)


    def test_update_boardmember_invalidboardid(self):  # testcase_47
        id = self.testinvalidid
        response = addmembertoboard(id,'divya', 'divya.hgreddy@gmail.com', 'normal')
        assert (response.status_code == 400)

    def test_update_boardmember_emptyemail(self):  # testcase_48
        id = self.testboardid
        response = addmembertoboard(id,'divya', '', 'normal')
        assert (response.status_code == 400)



    def test_update_boardmember_emptytype(self):  # testcase_49
        id = self.testboardid
        response = addmembertoboard(id, 'divya', 'divya.hgreddy@gmail.com', '')
        assert (response.status_code == 400)



    def test_update_boardmember_forbidden(self):  # testcase_50
        id = self.forbidden_id#another's board id
        response = addmembertoboard(id, 'divya', 'divya.hgreddy@gmail.com', 'normal')
        assert (response.status_code == 401)



    def test_update_specific_boardmember(self):#testcase_51
        id=self.testboardid
        ADDMEMBER = addmembertoboard(id, 'kavya G Rao', 'kavya.rao@hashedin.com', 'normal')
        idmember=getmemberid(id,'kavya G Rao')
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'admin'})
        assert (response.status_code==200)



    def test_update_specific_boardmember_invalid_key(self):#testcase_52
        id=self.testboardid
        ADDMEMBER = addmembertoboard(id, 'kavya G Rao', 'kavya.rao@hashedin.com', 'normal')
        idmember=getmemberid(id,'kavya G Rao')
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.testinvalidkey,'token':self.testinvalidtoken,'type':'admin'})
        assert (response.status_code==401)


    def test_update_specific_boardmember_invalid_boardid(self):#testcase_53
        id=self.testinvalidid
        ADDMEMBER = addmembertoboard(self.testboardid, 'kavya G Rao', 'kavya.rao@hashedin.com', 'normal')
        idmember = getmemberid(self.testboardid, 'kavya G Rao')
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'admin'})
        assert (response.status_code==400)


    def test_update_specific_boardmember_invalid_memberid(self):#testcase_54
        id=self.testboardid
        idmember=self.testinvalidid
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'admin'})
        assert (response.status_code==400)


    def test_update_specific_boardmember_invalid_membertype(self):#testcase_55
        id = self.testboardid
        ADDMEMBER = addmembertoboard(id, 'kavya G Rao', 'kavya.rao@hashedin.com', 'normal')
        idmember = getmemberid(id, 'kavya G Rao')
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':None})
        assert (response.status_code==400)


    def test_update_specific_boardmember_invalid_forbidden(self):#testcase_56
        id=self.forbidden_id#another's boardid
        idmember=self.testinvalidid
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'normal'})
        assert (response.status_code==401)


    def test_retrive_allfields_singleboard(self):#testcase_57
        id = self.testboardid
        resp=requests.get(self.url+id,params=self.payload)
        assert (resp.status_code==200)
        returnid=resp.json()['id']
        assert (returnid==id)


    def test_retrive_allfields_singleboard_invalidkey(self):#testcase_58
        id = self.testboardid
        resp=requests.get(self.url+id,params=self.payload.update({'key':self.testinvalidkey}))
        assert (resp.status_code==401)

    def test_retrive_allfields_singleboard_invalidboardid(self):  # testcase_59
        id = self.testinvalidid
        resp = requests.get(self.url + id, params=payload)
        assert (resp.status_code == 400)

    def test_retrive_allfields_singleboard_forbidden(self):  # testcase_60
        id = self.forbidden_id#another's id
        resp = requests.get(self.url + id, params=self.payload)
        assert (resp.status_code == 401)



    def test_retrive_specificfields_board(self):#testcase_61
        id=self.testboardid
        field="labelNames"
        resp = requests.get(self.url + id, params={'key':self.key,'token':self.token,'field':field})
        assert (resp.status_code==200)
        assert id == resp.json()['id']



    def test_retrive_specificfields_board_invalidkey(self):#testcase_62
        id=self.testboardid
        field="labelNames"
        resp = requests.get(self.url + id, params={'key':self.testinvalidkey,'token':self.token,'field':field})
        assert (resp.status_code==401)



    def test_retrive_specificfields_board_invalidBoardid(self):#testcase_63
        id=self.testinvalidid
        field="labelNames"
        resp = requests.get(self.url + id, params={'key':self.key,'token':self.token,'field':field})
        assert (resp.status_code==400)

    def test_retrive_specificfields_board_invalidfield(self):  # testcase_64
        id = self.testboardid
        field = None
        resp = requests.get(self.url + id+'/field', params={'key': self.key, 'token': self.token})
        assert (resp.status_code == 404)


if __name__=='__main__':
    pytest.main()

