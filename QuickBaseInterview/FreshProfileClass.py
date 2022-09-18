import email
import json
from tempfile import TemporaryDirectory

class FreshProfile:
    def __init__(self, name="", email="", jobtitle="", tags="", description="", avatar=""):
        self._name=name
        self._email=email
        self._jobtitle=jobtitle
        self._tags=tags
        self._description=description
        self._avatar=avatar 

    def _get_name(self):
        return self._name
    def _set_name(self, val):
        self._name = str(val)
    def _get_email(self):
        return self._email
    def _set_email(self, val):
        self._email = str(val)
        print(self._email)
    def _get_jobtitle(self):
        return self._jobtitle
    def _set_jobtitle(self, val):
        self._jobtitle = str(val)
    def _get_tags(self):
        return self._tags
    def _set_tags(self, val):
        self._tags = str(val)
    def _get_description(self):
        return self._description
    def _set_description(self, val):
        self._description = str(val)
    def _get_avatar(self):
        return self._avatar
    def _set_avatar(self, val):
        self._avatar = str(val)
    