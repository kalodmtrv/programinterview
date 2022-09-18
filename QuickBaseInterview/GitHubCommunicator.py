from urllib import response
import requests

from GitProfileClass import GitProfile


class GitHubCommunicator:
    def __init__(self, gitprofile = GitProfile()):
        self._gitprofile = gitprofile
        self._username =""
        self._response =""

    
    def _get_gitprofile(self):
        return self._gitprofile
    def _set_gitprofile(self, val):
        self._gitprofile = val
    def _get_username(self):
        return self._username
    def _set_username(self, val):
        self._username = str(val)
    def _get_response(self):
        return self._response
    def _set_response(self, val):
        self._response = str(val)

    def call_api(self, user):
        apiEndpointBase = "https://api.github.com/users/{}"
        if(len(user)<=0):
            return
        userEndpoint = apiEndpointBase.format(user)
        apiResponse = requests.get(userEndpoint)
        if(not apiResponse.ok):
            return
        self._response = apiResponse.text
        
    def get_git_profile_info(self):
        if(len(self._get_response())<=0):
            return
        self._get_gitprofile().parseFromJson(self._get_response())
        return self._get_gitprofile()

   

    