import email
import json
from tempfile import TemporaryDirectory


class GitProfile:
    def __init__(self, name="", email="", company="", id=""):
        self._name = name
        self._email = email
        self._company = company
        self._id = id
        
    def _get_name(self):
        return self._name
    def _set_name(self, val):
        self._name = str(val)
    def _get_email(self):
        return self._email
    def _set_email(self, val):
        self._email = str(val)
    def _get_company(self):
        return self._company
    def _set_company(self, val):
        self._company = str(val)
    def _get_id(self):
        return self._id
    def _set_id(self, val):
        self._id = str(val)
    
    



    def parseFromJson(self, jsonString):
        if len(jsonString) <= 0: return 
        tempDict = json.loads(jsonString)
        if (("id" in tempDict) and ("login" in tempDict) and ("company" in tempDict) and ("email" in tempDict)):
            self._set_company(tempDict.get("company"))
            self._set_email(tempDict.get("email"))
            self._set_name(tempDict.get("login"))
            self._set_id(tempDict.get("id"))
            
