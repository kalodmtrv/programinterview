from ast import parse
from cgi import test
import unittest
import json
import sys  
sys.path.insert(1, 'C:/Users/User/Desktop/QuickBaseInterview')
import FreshProfileClass

class TestFreshProfileClass(unittest.TestCase):
    def testGetterName(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        self.assertEquals("testname", testProfile._get_name())

    def testSetterName(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        testProfile._set_name("NewTestName")
        self.assertEquals("NewTestName", testProfile._get_name()) 

    def testGetterEmail(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        self.assertEquals("testemail", testProfile._get_email())

    def testSetterEmail(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        testProfile._set_email("NewTestEmail")
        self.assertEquals("NewTestEmail", testProfile._get_email())

    def testGetterJobTitle(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        self.assertEquals("testjobtitle", testProfile._get_jobtitle())

    def testSetterJobTitle(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        testProfile._set_jobtitle("NewTestJobTitle")
        self.assertEquals("NewTestJobTitle", testProfile._get_jobtitle())
    
    def testGetterTags(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        self.assertEquals("testtags", testProfile._get_tags())

    def testSetterTags(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        testProfile._set_tags("NewTestTags")
        self.assertEquals("NewTestTags", testProfile._get_tags())

    def testGetterDescription(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        self.assertEquals("testdescription", testProfile._get_description())

    def testSetterDescription(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        testProfile._set_description("NewTestDescription")
        self.assertEquals("NewTestDescription", testProfile._get_description())

    def testGetterAvatar(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        self.assertEquals("testavatar", testProfile._get_avatar())

    def testSetterAvatar(self):
        testProfile = FreshProfileClass.FreshProfile("testname","testemail","testjobtitle","testtags","testdescription","testavatar")
        testProfile._set_avatar("NewTestAvatar")
        self.assertEquals("NewTestAvatar", testProfile._get_avatar())