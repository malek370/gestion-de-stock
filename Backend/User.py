import time
import json
from flask import Flask,request,jsonify,render_template,redirect ,url_for ,session
class User:
    def __init__(self,username,password,role):
        self.username=username
        self.password=password
        self.creationDate=time.time()
        self.role=role
    def getUser(self):
        return json.dumps(self.__dict__)