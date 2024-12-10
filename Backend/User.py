import time
import json
import uuid 
  
 
class User:
    def __init__(self,username,password,role):
        self.username=username
        self.password=password
        self.creationDate=time.time()
        self.role=role
        self.PublicId= uuid.uuid4().hex

    def dict(self):
        if self.username == None or self.password == None or self.role==None:
            raise Exception("invalid inputs")
        else:
            return self.__dict__