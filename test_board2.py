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
    def test_update_board_INVALID_KEY(self):#testcase_42
        id="5c610bdaef382018a436b32e"
        response=requests.put(self.url+id,params={'key':'dscs','token':self.token,'name':'divya hg'})
        assert (response.status_code==401)

    def test_update_board_INVALID_boardid(self):  # testcase_43
        id = "aasskk"
        response = requests.put(self.url + id, params={'key': self.key, 'token': self.token, 'name': 'divya hg'})
        assert (response.status_code == 400)

    def test_update_board(self):#testcase_44
        id="5c616913e3fca870309fd37a"
        response=requests.put(self.url+id,params={'key':self.key,'token':self.token,'name':'divya hg'})
        assert (response.status_code==401)
    def test_update_boardmember(self):#testcase_45
        id="5c610bdaef382018a436b32e"
        response=requests.put(self.url+id+'/members',params={'key':self.key,'token':self.token,'fullName':'ankkit249012',
                                                             'email':'abcd@xyz.com','type':'normal'})
        assert (response.status_code==200)

    def test_update_boardmember_invalidkey(self):  # testcase_46
        id = "5c610bdaef382018a436b32e"
        response = requests.put(self.url + id + '/members',
                                params={'key': 'ssssddd', 'token': 'ssds', 'fullName': 'ankkit249012',
                                        'email': 'abcd@xyz.com', 'type': 'normal'})
        assert (response.status_code == 401)
    def test_update_boardmember_invalidboardid(self):  # testcase_47
        id = "xxxsss"
        response = requests.put(self.url + id + '/members',
                                params={'key': self.key, 'token': self.token, 'fullName': 'ankkit249012',
                                        'email': 'abcd@xyz.com', 'type': 'normal'})
        assert (response.status_code == 400)

    def test_update_boardmember_emptyemail(self):  # testcase_48
        id = "5c610bdaef382018a436b32e"
        response = requests.put(self.url + id + '/members',
                                params={'key': self.key, 'token': self.token, 'fullName': 'ankkit249012',
                                        'email': None, 'type': 'normal'})
        assert (response.status_code == 400)
    def test_update_boardmember_emptytype(self):  # testcase_49
        id = "5c610bdaef382018a436b32e"
        response = requests.put(self.url + id + '/members',
                                params={'key': self.key, 'token': self.token, 'fullName': 'ankkit249012',
                                        'email': 'abcd@xyz.com', 'type': ''})
        assert (response.status_code == 400)
    def test_update_boardmember_forbidden(self):  # testcase_50
        id = "5c616913e3fca870309fd37a"
        response = requests.put(self.url + id + '/members',
                                params={'key': self.key, 'token': self.token, 'fullName': 'ankkit249012',
                                        'email': 'abcd@xyz.com', 'type': 'admin'})
        assert (response.status_code == 401)
    def test_update_specific_boardmember(self):#testcase_51
        id="5c616a0f0e01197a3562a289"
        idmember="5c60f71ca2a4b77022e377fd"
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'admin'})
        assert (response.status_code==200)
        returnvalue=response.json()['memberships'][0]['memberType']
        assert (returnvalue=='admin')
    def test_update_specific_boardmember_invalid_key(self):#testcase_52
        id="5c616a0f0e01197a3562a289"
        idmember="5c60f71ca2a4b77022e377fd"
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':'aaxx','token':self.token,'type':'admin'})
        assert (response.status_code==401)
    def test_update_specific_boardmember_invalid_boardid(self):#testcase_53
        id="aaaa"
        idmember="5c60f71ca2a4b77022e377fd"
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'admin'})
        assert (response.status_code==400)
    def test_update_specific_boardmember_invalid_memberid(self):#testcase_54
        id="5c616a0f0e01197a3562a289"
        idmember=""
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'admin'})
        assert (response.status_code==400)
    def test_update_specific_boardmember_invalid_membertype(self):#testcase_55
        id="5c616a0f0e01197a3562a289"
        idmember="5c60f71ca2a4b77022e377fd"
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':None})
        assert (response.status_code==400)
    def test_update_specific_boardmember_invalid_membertype(self):#testcase_56
        id="5c616913e3fca870309fd37a"
        idmember="5c60f71ca2a4b77022e377fd"
        response=requests.put(self.url+id+'/members/'+idmember,params={'key':self.key,'token':self.token,'type':'normal'})
        assert (response.status_code==403)
    def test_retrive_allfields_singleboard(self):#testcase_57
        id = "5c616913e3fca870309fd37a"
        resp=requests.get(self.url+id,params=self.payload)
        assert (resp.status_code==200)
        returnid=resp.json()['id']
        assert (returnid==id)
    def test_retrive_allfields_singleboard_invalidkey(self):#testcase_58
        id = "5c616913e3fca870309fd37a"
        resp=requests.get(self.url+id,params=self.payload.update({'key':'xxxxx'}))
        assert (resp.status_code==401)

    def test_retrive_allfields_singleboard_invalidboardid(self):  # testcase_59
        id = "xxxxx"
        resp = requests.get(self.url + id, params=self.payload)
        assert (resp.status_code == 400)

    def test_retrive_allfields_singleboard_forbidden(self):  # testcase_60
        id = "5c618c396220596250a10d64"
        resp = requests.get(self.url + id, params=self.payload)
        assert (resp.status_code == 401)
    def test_retrive_specificfields_board(self):#testcase_61
        id="5c616913e3fca870309fd37a"
        field="labelNames"
        resp = requests.get(self.url + id, params={'key':self.key,'token':self.token,'field':field})
        assert (resp.status_code==200)
        assert id == resp.json()['id']
    def test_retrive_specificfields_board_invalidkey(self):#testcase_62
        id="5c616913e3fca870309fd37a"
        field="labelNames"
        resp = requests.get(self.url + id, params={'key':'xxxx','token':self.token,'field':field})
        assert (resp.status_code==401)
    def test_retrive_specificfields_board_invalidBoardid(self):#testcase_63
        id="xxxx"
        field="labelNames"
        resp = requests.get(self.url + id, params={'key':self.key,'token':self.token,'field':field})
        assert (resp.status_code==400)












if __name__=='__main__':
    pytest.main()

