import pytest
import json
import requests

from Helper import *


class Test_board_push:
    @classmethod
    def setup_class(cls):
        with open('data.json','r') as data:
            data=json.load(data)
        cls.key=data['key']
        cls.token=data['token']
        cls.url=data['url']
        cls.name=data['uname']
        cls.testinvalidkey=data['testinvalidkey']
        cls.testinvalidtoken=data['testinvalidtoken']
        cls.testinvalidid=data['testinvalidid']
        cls.payload={'key':cls.key,'token':cls.token,'name':cls.name}
        createboard(payload)
        cls.testboardid=getid('test_BOARD')
    def teardown_method(self):
        print(deleteboard(self.testboardid))

    def test_newboard(self):#TestCase_1
        response=createboard()
        assert (response.status_code==200)
        board_id=response.json()['id']
        response=requests.get(self.url+'/'+board_id,params=self.payload)
        assert (response.json()['id']==board_id)
        deleteboard(id)
    def test_newboard_invalid_keyortoken(self):#TestCase_2
        response=createboard({'key':self.testinvalidkey,'token':self.testinvalidtoken})
        assert (response.status_code==401)
    def test_newboard_inavlid_name(self):#TestCase_3
        response = createboard({'key':self.key,'token':self.token,'name':None})
        print(self.payload)
        assert (response.status_code == 400)
    '''def test_newboard_forbidden(self):#testcase_4
        response = createboard()
        print(self.payload)'''
    '''def test_calenderkey(self):#TestCase_5
        iid="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key': self.key, 'token': self.token})
        assert (response.status_code == 200)'''
    def test_calenderkey_invalid_id(self):#TestCase_6
        id=self.testinvalidid
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key': self.key, 'token': self.token})
        assert (response.status_code == 400)

    def test_calenderkey_invalid_token_key(self):#TestCase_7
        id = self.testboardid
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key':self.testinvalidkey, 'token': self.testinvalidtoken})
        assert (response.status_code == 401)
        deleteboard(id)

    def test_calenderkey_forbidden(self):#TestCase_8
        id=self.testboardid
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key':self.key, 'token': self.token})
        assert (response.status_code == 403)

    '''def test_newchecklist(self):#testcase_9
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/checklists",params=self.payload)
        assert (response.status_code == 200)'''
    def test_checklist_invalidkey(self):#TestCase_10
        id = self.testboardid
        response = requests.post(self.url + id + "/checklists", params={'key':self.testinvalidkey, 'token': self.testinvalidtoken})
        assert (response.status_code == 401)

    def test_checklist_invalidboardid(self):#TestCase_11
        id = self.testinvalidkey
        response = requests.post(self.url + id + "/checklists", params=self.payload)
        assert (response.status_code == 400)
    def test_checklist_invalid_name(self):#TestCase_12
        id = self.testinvalidkey
        response = requests.post(self.url + id + "/checklists", params={'key':self.key,'token':self.token,'name':None})
        assert (response.status_code == 400)
    '''def test_checklist_forbidden(self):#TestCase_13
        id = "5c616913e3fca870309fd37a"
        response = requests.post(self.url + id + "/checklists", params=self.payload)
        assert (response.status_code == 403)'''
    def test_new_emailkey(self):#testcase_14
        createboard({'key':self.key,'token':self.token,'name':'test_emailkey'})
        id=getid('test_emailkey')
        response=requests.post(self.url+id+"/emailKey/generate",params=self.payload)
        assert (response.status_code==200)
    def test_emailkey_invalidkey(self):#testcase_15
        id = self.testboardid
        response = requests.post(self.url + id + "/emailKey/generate", params={'key':self.testinvalidkey, 'token': self.testinvalidtoken})
        assert (response.status_code == 401)

    def test_emailkey_invalid_boardid(self):#testcase_16
        id = self.testinvalidid
        response = requests.post(self.url + id + "/emailKey/generate", params=self.payload)
        assert (response.status_code == 400)

    def test_create_lablel(self):#testcase_17
        id = self.testboardid
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':'ankitpatnaik','color':'blue'})
        assert (response.status_code == 200)
        color=response.json()['color']
        assert (color=='blue')
        deleteboard(id)

    def test_create_lablel_invalidkey(self):#testcase_18
        id = self.testboardid
        response=requests.post(self.url+id+"/labels",params={'key':self.testinvalidkey,'token':self.testinvalidtoken,'name':'ankitpatnaik','color':'blue'})
        assert (response.status_code == 401)
    def test_create_lablel_invalid_id(self):#testcase_19
        id=self.testinvalidid
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':'ankitpatnaik','color':'blue'})
        assert (response.status_code == 400)
    def test_create_lablel_invalid_name(self):#testcase_20
        id=self.testinvalidkey
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':None,'color':'blue'})
        assert (response.status_code == 400)
    def test_create_lablel_invalid_color(self):#testcase_21
        id=self.testboardid
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':'ankit22','color':' '})
        assert (response.status_code == 400)
    '''def test_create_label_forbidden(self):#testcase_22
        id = "5c616913e3fca870309fd37a"
        response = requests.post(self.url + id + "/labels",params={'key': self.key, 'token': self.token, 'name': 'ankit22', 'color':'black'})
        assert (response.status_code == 403)'''
    def test_list_create(self):#testcase_23
        id=self.testboardid
        response=requests.post(self.url+id+"/lists",params={'key': self.key, 'token': self.token, 'name': 'ankit22','pos':'top'})
        assert (response.status_code==200)
    def test_list_create_invalid_key(self):#testcase_24
        id=self.testinvalidkey
        response=requests.post(self.url+id+"/lists",params={'key': 'dfddd', 'token': self.token, 'name': 'ankit22','pos':'top'})
        assert (response.status_code==401)
    def test_list_create_invalid_id(self):#testcase_25
        id=self.testinvalidid
        response=requests.post(self.url+id+"/lists",params={'key': self.key, 'token': self.token, 'name': 'ankit22','pos':'top'})
        assert (response.status_code==400)
    def test_list_create_invalid_name(self):#testcase_26
        id=self.testboardid
        response=requests.post(self.url+id+"/lists",params={'key': self.key, 'token': self.token, 'name': None,'pos':'top'})
        assert (response.status_code==400)

    def test_list_create_invalid_position(self):  # testcase_27
        id = self.testboardid
        response = requests.post(self.url + id + "/lists",
                                 params={'key': self.key, 'token': self.token, 'name': 'ankit', 'pos': 'kjbhkjb'})
        assert (response.status_code == 400)

    def test_list_create_forbidden(self):  # testcase_28
        id = "5c618c396220596250a10d64"#id of another's board
        response = requests.post(self.url + id + "/lists",
                                 params={'key': self.key, 'token': self.token, 'name': 'ankit', 'pos': 'top'})
        assert (response.status_code == 401)
    '''def test_markviewed(self):#testcase_29
        id="5c616913e3fca870309fd37a"
        response = requests.post(self.url + id,
                                 params=self.payload)
        assert (response.status_code == 200)'''
    def test_delete_board(self):#testcase_33---DELETE CASE
        response = createboard()
        id = response.json()['id']
        response=requests.delete(self.url+id+'/',params=self.payload)
        assert (response.status_code==200)
        try:
            response = requests.get(self.url + '/' + id, params=self.payload)
        except:
            assert (id!=response.json()['id'])

    def test_delete_board_invalid_key(self):#testcase_34
        id = self.testboardid
        response=requests.delete(self.url+id+'/',params={'key':self.testinvalidkey,'token':self.testinvalidtoken})
        assert (response.status_code==401)
        try:
            response = requests.get(self.url + '/' + id, params=self.payload)
        except:
            assert (id!=response.json()['id'])

    def test_delete_board_invalid_ID(self):#testcase_35
            id = self.testinvalidid
            response=requests.delete(self.url+id+'/',params=self.payload)
            assert (response.status_code==400)
            try:
                response = requests.get(self.url + '/' + id, params=self.payload)
            except:
                assert (id!=response.json()['id'])

    def test_delete_board_FORBIDDEN(self):#testcase_36
          id = "5c618c396220596250a10d64"#another board's id
          response=requests.delete(self.url+id+'/',params=self.payload)
          assert (response.status_code==401)
    def test_delete_board_member(self):#testcase_37---DELETE CASE
        id=self.testboardid
        addmember=addmembertoboard(id,'ankit','ankitkumarpatnaik001@gmail.com','normal')
        idmember=getmemberid(id,'ankit')
        response=requests.delete(self.url+id+"/members/"+idmember,params=self.payload)
        assert (response.status_code==200)
    def test_delete_board_member_invalidKey(self):#testcase_38
        id = self.testboardid
        addmember = addmembertoboard(id, 'ankit', 'ankitkumarpatnaik001@gmail.com', 'normal')
        idmember = getmemberid(id, 'ankit')
        response=requests.delete(self.url+id+"/members/"+idmember,params={'key':self.testinvalidkey,'token':self.testinvalidtoken})
        assert (response.status_code==401)
    def test_delete_board_member_invalidBOARD_ID(self):#testcase_39
        id = self.testinvalidid
        idmember=self.testboardid
        response=requests.delete(self.url+id+"/members/"+idmember,params=self.payload)
        assert (response.status_code==400)
    def test_delete_board_member_FORBIDDEN(self):#testcase_40
            id="5c618c396220596250a10d64"#another's board id
            idmember=self.testboardid
            response=requests.delete(self.url+id+"/members/"+idmember,params=self.payload)
            assert (response.status_code==401)













if __name__=='__main__':
    pytest.main()













































