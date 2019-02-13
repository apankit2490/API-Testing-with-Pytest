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
        print("teardown"+str(deleteboard(self.testboardid,self.payload)))
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
        deleteboard(bid)


    def test_moveAllCards(self):
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


    def test_moveAllCards_invalidid(self):
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
    def test_moveAllCards_invalidkey(self):
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







if __name__=='__main__':
    pytest.main()  