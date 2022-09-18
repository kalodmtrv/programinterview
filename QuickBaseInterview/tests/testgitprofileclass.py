from ast import parse
from cgi import test
import unittest
import json
import sys  
sys.path.insert(1, 'C:/Users/User/Desktop/QuickBaseInterview')
import GitProfileClass

class TestGitProfileClass(unittest.TestCase):
    def testGetterName(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        self.assertEquals("testname", testProfile._get_name())

    def testSetterName(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        testProfile._set_name("NewTestName")
        self.assertEquals("NewTestName", testProfile._get_name())
    
    def testGetterEmail(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        self.assertEquals("testemail", testProfile._get_email())

    def testSetterEmail(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        testProfile._set_email("NewTestEmail")
        self.assertEquals("NewTestEmail", testProfile._get_email())

    def testGetterCompany(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        self.assertEquals("testcompany", testProfile._get_company())

    def testSetterCompany(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        testProfile._set_company("NewTestCompany")
        self.assertEquals("NewTestCompany", testProfile._get_company())

    def testGetterID(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        self.assertEquals("testid", testProfile._get_id())

    def testSetterID(self):
        testProfile = GitProfileClass.GitProfile("testname","testemail","testcompany","testid")
        testProfile._set_id("NewTestID")
        self.assertEquals("NewTestID", testProfile._get_id())

    def testParseJson(self):
        testProfile = GitProfileClass.GitProfile()
        testResponse = '{"login":"testuserinterv","id":113466077,"node_id":"U_kgDOBsNa3Q","avatar_url":"https://avatars.githubusercontent.com/u/113466077?v=4","gravatar_id":"","url":"https://api.github.com/users/testuserinterv","html_url":"https://github.com/testuserinterv","followers_url":"https://api.github.com/users/testuserinterv/followers","following_url":"https://api.github.com/users/testuserinterv/following{/other_user}","gists_url":"https://api.github.com/users/testuserinterv/gists{/gist_id}","starred_url":"https://api.github.com/users/testuserinterv/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/testuserinterv/subscriptions","organizations_url":"https://api.github.com/users/testuserinterv/orgs","repos_url":"https://api.github.com/users/testuserinterv/repos","events_url":"https://api.github.com/users/testuserinterv/events{/privacy}","received_events_url":"https://api.github.com/users/testuserinterv/received_events","type":"User","site_admin":false,"name":null,"company":null,"email":null}'
        testProfile.parseFromJson(testResponse)
        self.assertEquals("113466077",  testProfile._get_id())