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
    '''def test_newboard_forbidden(self):#testcase_4
        response = requests.post(self.url, params={'key': self.key, 'token': self.token, 'name': None})
        print(self.payload)'''
    '''def test_calenderkey(self):#TestCase_5
        iid="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key': self.key, 'token': self.token})
        assert (response.status_code == 200)'''
    def test_calenderkey_invalid_id(self):#TestCase_6
        id="5c615ba7f5c7564b8f9esdssd8c43"
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key': self.key, 'token': self.token})
        assert (response.status_code == 400)

    def test_calenderkey_invalid_token_key(self):#TestCase_7
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key':'sdfs', 'token': self.token})
        assert (response.status_code == 401)

    def test_calenderkey_forbidden(self):#TestCase_8
        id="5c616913e3fca870309fd37a"
        response=requests.post(self.url+id+"/calendarKey/generate",params={'key':self.key, 'token': self.token})
        assert (response.status_code == 403)
    '''def test_newchecklist(self):#testcase_9
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/checklists",params=self.payload)
        assert (response.status_code == 200)'''
    def test_checklist_invalidkey(self):#TestCase_10
        id = "5c615ba7f5c7564b8f9e8c43"
        response = requests.post(self.url + id + "/checklists", params={'key':'sdfs', 'token': self.token})
        assert (response.status_code == 401)
    def test_checklist_invalidboardid(self):#TestCase_11
        id = "5c615ba7sdsf5c7564b8f9e8c43"
        response = requests.post(self.url + id + "/checklists", params=self.payload)
        assert (response.status_code == 400)
    def test_checklist_invalid_name(self):#TestCase_12
        id = "5c615ba7f5c7564b8f9e8c43"
        response = requests.post(self.url + id + "/checklists", params={'key':self.key,'token':self.token,'name':None})
        assert (response.status_code == 400)
    '''def test_checklist_forbidden(self):#TestCase_13
        id = "5c616913e3fca870309fd37a"
        response = requests.post(self.url + id + "/checklists", params=self.payload)
        assert (response.status_code == 403)'''
    def test_new_emailkey(self):#testcase_14
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/emailKey/generate",params=self.payload)
        assert (response.status_code==200)
    def test_emailkey_invalidkey(self):#testcase_15
        id = "5c615ba7f5c7564b8f9e8c43"
        response = requests.post(self.url + id + "/emailKey/generate", params={'key':'sdfs', 'token': self.token})
        assert (response.status_code == 401)

    def test_emailkey_invalid_boardid(self):#testcase_16
        id = "5c615ba7f5c756sdsddsddd4b8f9e8c43"
        response = requests.post(self.url + id + "/emailKey/generate", params=self.payload)
        assert (response.status_code == 400)

    def test_create_lablel(self):#testcase_17
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':'ankitpatnaik','color':'blue'})
        assert (response.status_code == 200)
        color=response.json()['color']
        assert (color=='blue')

    def test_create_lablel_invalidkey(self):#testcase_18
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/labels",params={'key':'sasas','token':self.token,'name':'ankitpatnaik','color':'blue'})
        assert (response.status_code == 401)
    def test_create_lablel_invalid_id(self):#testcase_19
        id="5c615ba7f5c7564b8sdsdf9e8c43"
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':'ankitpatnaik','color':'blue'})
        assert (response.status_code == 400)
    def test_create_lablel_invalid_name(self):#testcase_20
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':None,'color':'blue'})
        assert (response.status_code == 400)
    def test_create_lablel_invalid_color(self):#testcase_21
        id="5c615ba7f5c7564b8f9e8c43"
        response=requests.post(self.url+id+"/labels",params={'key':self.key,'token':self.token,'name':'ankit22','color':' '})
        assert (response.status_code == 400)
    '''def test_create_label_forbidden(self):#testcase_22
        id = "5c616913e3fca870309fd37a"
        response = requests.post(self.url + id + "/labels",params={'key': self.key, 'token': self.token, 'name': 'ankit22', 'color':'black'})
        assert (response.status_code == 403)'''
    def test_list_create(self):#testcase_23
        id="5c616913e3fca870309fd37a"
        response=requests.post(self.url+id+"/lists",params={'key': self.key, 'token': self.token, 'name': 'ankit22','pos':'top'})
        assert (response.status_code==200)
    def test_list_create_invalid_key(self):#testcase_24
        id="5c616913e3fca870309fd37a"
        response=requests.post(self.url+id+"/lists",params={'key': 'dfddd', 'token': self.token, 'name': 'ankit22','pos':'top'})
        assert (response.status_code==401)
    def test_list_create_invalid_id(self):#testcase_25
        id="5c616913e3fca87030adsdsd9fd37a"
        response=requests.post(self.url+id+"/lists",params={'key': self.key, 'token': self.token, 'name': 'ankit22','pos':'top'})
        assert (response.status_code==400)
    def test_list_create_invalid_name(self):#testcase_26
        id="5c616913e3fca870309fd37a"
        response=requests.post(self.url+id+"/lists",params={'key': self.key, 'token': self.token, 'name': None,'pos':'top'})
        assert (response.status_code==400)

    def test_list_create_invalid_position(self):  # testcase_27
        id = "5c616913e3fca870309fd37a"
        response = requests.post(self.url + id + "/lists",
                                 params={'key': self.key, 'token': self.token, 'name': 'ankit', 'pos': 'kjbhkjb'})
        assert (response.status_code == 400)

    '''def test_list_create_forbidden(self):  # testcase_28
        id = "5c616913e3fca870309fd37a"
        response = requests.post(self.url + id + "/lists",
                                 params={'key': self.key, 'token': self.token, 'name': 'ankit', 'pos': 'top'})
        assert (response.status_code == 403)'''
    '''def test_markviewed(self):#testcase_29
        id="5c616913e3fca870309fd37a"
        response = requests.post(self.url + id,
                                 params=self.payload)
        assert (response.status_code == 200)'''
    '''def test_delete_board(self):#testcase_33---DELETE CASE
        id = "5c61576a9e83e20f3781f091"
        response=requests.delete(self.url+id+'/',params=self.payload)
        assert (response.status_code==200)
        try:
            response = requests.get(self.url + '/' + id, params=self.payload)
        except:
            assert (id!=response.json()['id'])'''

    def test_delete_board_invalid_key(self):#testcase_34
        id = "5c6157a6f9de98516834e643"
        response=requests.delete(self.url+id+'/',params={'key':'vjadcvja','token':'asa'})
        assert (response.status_code==401)
        try:
            response = requests.get(self.url + '/' + id, params=self.payload)
        except:
            assert (id!=response.json()['id'])

    def test_delete_board_invalid_ID(self):#testcase_35
            id = "dfsfds"
            response=requests.delete(self.url+id+'/',params=self.payload)
            assert (response.status_code==400)
            try:
                response = requests.get(self.url + '/' + id, params=self.payload)
            except:
                assert (id!=response.json()['id'])

    def test_delete_board(self):#testcase_36
          id = "5c616913e3fca870309fd37a"
          response=requests.delete(self.url+id+'/',params=self.payload)
          assert (response.status_code==401)









































if __name__=='__main__':
    pytest.main()