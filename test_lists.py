import pytest
from Helper_lists import *
import json
import requests

class Test_list:

    @classmethod
    def setup_class(cls):
        with open('list_data.json', 'r') as data:
            data = json.load(data)
        cls.key = data['key']
        cls.token = data['token']
        cls.url = data['url']
        cls.name = data['uname']
        cls.payload = {'key': cls.key, 'token': cls.token, 'name': cls.name}
        cls.testinvalidkey = data['testinvalidkey']
        cls.testinvalidtoken = data['testinvalidtoken']
        cls.testinvalidid = data['testinvalidid']
        cls.payload = {'key': cls.key, 'token': cls.token, 'name': cls.name}
        createboard(cls.payload)
        cls.testboardid = getid('test_list')
        cls.forbidden_id = data['forbidden_id']
        cls.forbidden_Lid=data['forbidden_lid']

    def teardown_class(self):
        print("teardown"+str(deleteboard(self.testboardid,payload)))

    # def setup_method(self):
    #     with open('list_data.json','r') as data:
    #         data=json.load(data)
    #     self.key = data['key']
    #     self.token = data['token']
    #     self.url = data['url']
    #     self.url_list=data['url_list']
    #     self.name = data['uname']
    #     self.testinvalidkey = data['testinvalidkey']
    #     self.testinvalidtoken = data['testinvalidtoken']
    #     self.testinvalidid = data['testinvalidid']
    #     self.payload = {'key': self.key, 'token': self.token, 'name': self.name}
    #     y=name
    #     x=createboard(self.payload)
    #     print(x)
    #     self.testboardid = getid(y)
    #     self.forbidden_id = data['forbidden_id']
    #     self.forbidden_Lid=data['forbidden_lid']

    # def teardown_method(self):
    #     z=self.testboardid
    #     print(deleteboard(z))




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

    def test_createlist_forbidden(self):  # testcase_4
        gid = self.forbidden_id
        response = createlist(gid, 'ankit')
        assert (response.status_code == 401)

    def test_archiveallcards(self):# testcase_5
        bid=self.testboardid
        createlist(bid,'test_archive')
        lid=getlistid(bid,'test_archive')
        createcard(lid,'hello')
        response=requests.post(url_list+'/'+lid+'/archiveAllCards',params=payload)
        assert (response.status_code==200)



    def test_archiveallcards_invalidkey(self):# testcase_6
        bid=self.testboardid
        createlist(bid,'test_archive')
        lid=getlistid(bid,'test_archive')
        createcard(lid,'hello')
        response=requests.post(url_list+'/'+lid+'/archiveAllCards',params=payload.update({'key':self.testinvalidkey,'token':self.testinvalidtoken}))
        assert (response.status_code==401)


    def test_archiveallcards_invalidLid(self):# testcase_7
        bid = self.testboardid
        createlist(bid, 'test_archive')
        lid = self.testinvalidid
        response = requests.post(url_list + '/' + lid + '/archiveAllCards', params=self.payload)
        assert (response.status_code == 400)


    def test_archiveallcards_forbidden(self):  # testcase_8
        bid = self.testboardid
        createlist(bid, 'test_archive')
        lid = self.forbidden_Lid
        response = requests.post(url_list + '/' + lid + '/archiveAllCards', params=payload)
        assert (response.status_code == 401)


    def test_moveAllCards(self):#testcase_9
        createboard({'key':key,'token':token,'name':'xyz'})
        bid=getid('xyz')
        createlist(bid,'sourcecards')
        slid=getlistid(bid,'sourcecards')
        createcard(slid,'card1')
        createlist(bid,'destcards')
        dlid=getlistid(bid,'destcards')
        response=requests.post(url_list+'/'+slid+'/moveAllCards',params={'key':key,'token':token,'idBoard':bid,'idList':dlid})
        assert response.status_code==200
        deleteboard(bid)


    def test_moveAllCards_invalidid(self):#testcase_10
        createboard({'key':key,'token':token,'name':'xyz'})
        bid=getid('xyz')
        createlist(bid,'sourcecards')
        slid=getlistid(bid,'sourcecards')
        createcard(slid,'card1')
        createlist(bid,'destcards')
        dlid=getlistid(bid,'destcards')
        response=requests.post(url_list+'/'+slid+'/moveAllCards',params={'key':key,'token':token,'idBoard':self.testinvalidid,'idList':dlid})
        assert response.status_code==400
        deleteboard(bid)


    def test_moveAllCards_invalidkey(self):#testcase_11
        createboard({'key':key,'token':token,'name':'xyz'})
        bid=getid('xyz')
        createlist(bid,'sourcecards')
        slid=getlistid(bid,'sourcecards')
        createcard(slid,'card1')
        createlist(bid,'destcards')
        dlid=getlistid(bid,'destcards')
        response=requests.post(url_list+'/'+slid+'/moveAllCards',params={'key':self.testinvalidkey,'token':self.testinvalidtoken,'idBoard':bid,'idList':dlid})
        assert response.status_code==401
        deleteboard(bid)


    def test_moveAllCards_invalid_list_id(self):#testcase_12
        createboard({'key':key,'token':token,'name':'xyz'})
        self.bid=getid('xyz')
        createlist(self.bid,'sourcecards')
        slid=self.testinvalidid
        dlid=getlistid(self.bid,'destcards')
        response=requests.post(url_list+'/'+slid+'/moveAllCards',params={'key':key,'token':token,'idBoard':self.testinvalidid,'idList':dlid})
        assert response.status_code==400
        deleteboard(self.bid)


    def test_retrive_single_list(self):#testcase_13
        bid = self.testboardid
        createlist(bid, 'test_archive')
        lid = getlistid(bid, 'test_archive')
        createcard(lid,'hello')
        response=requests.get(url_list+'/'+lid,params=self.payload)
        assert (response.status_code==200)
        returnid=response.json()['id']
        assert (lid==returnid)

    def test_retrive_single_list_invalid_key(self):#testcase_14
        bid = self.testboardid
        createlist(bid, 'test_list2')
        lid = getlistid(bid, 'test_list2')
        response = requests.get(url_list + '/' + lid, params={'key':self.testinvalidkey,'token':self.testinvalidtoken})
        assert (response.status_code == 401)

    def test_retrive_single_list_invalid_listid(self):#testcase_15
        bid = self.testboardid
        createlist(bid, 'hello')
        lid = self.testinvalidid
        response = requests.get(url_list + '/' + lid, params=self.payload)
        assert (response.status_code == 400)
    def test_retrive_specific_field(self):
        bid = self.testboardid
        createlist(bid, 'test_archive')
        lid = getlistid(bid, 'test_archive')
        createcard(lid, 'hello')
        field='name'
        response = requests.get(url_list + '/' + lid+'/'+field,params=self.payload)
        assert (response.status_code == 200)
    def test_retrive_specific_field_invalidkey(self):
        bid = self.testboardid
        createlist(bid, 'test_archive')
        lid = getlistid(bid, 'test_archive')
        createcard(lid, 'hello')
        field='name'
        response = requests.get(url_list + '/' + lid+'/'+field,params={'key':self.testinvalidkey})
        assert (response.status_code == 401)

    def test_retrive_specific_field_invalid_listid(self):
        bid = self.testboardid
        createlist(bid, 'test_archive')
        lid = self.testinvalidid
        field = 'name'
        response = requests.get(url_list + '/' + lid + '/' + field, params=self.payload)
        assert (response.status_code == 400)







if __name__=='__main__':
    pytest.main()  