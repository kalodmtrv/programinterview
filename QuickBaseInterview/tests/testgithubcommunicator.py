from ast import parse
from cgi import test
import unittest
import json
import sys  
sys.path.insert(1, 'C:/Users/User/Desktop/QuickBaseInterview')
import GitHubCommunicator
import GitProfileClass

class TestGitHubCommunicator(unittest.TestCase):
    def testGetterGitProfile(self):
        testGitProfile = GitProfileClass.GitProfile("testname")
        testCommunicator = GitHubCommunicator.GitHubCommunicator(testGitProfile)
        self.assertEquals("testname", testCommunicator._get_gitprofile()._get_name())
    def testSetterGitProfile(self):
        testGitProfile = GitProfileClass.GitProfile("testname")
        testCommunicator = GitHubCommunicator.GitHubCommunicator(testGitProfile)
        testGitProfile._set_name("newName")
        testCommunicator._set_gitprofile(testGitProfile)
        self.assertEquals("newName", testCommunicator._get_gitprofile()._get_name())
    def testGetUserData(self):
        testCommunicator = GitHubCommunicator.GitHubCommunicator()
        testCommunicator.call_api("testuserinterv")
    def testgetProfile(self):
        testCommunicator = GitHubCommunicator.GitHubCommunicator()
        testCommunicator.call_api("testuserinterv")
        prof = testCommunicator.get_git_profile_info()