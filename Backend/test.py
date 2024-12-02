# import random

# from functools import wraps
# from flask import Flask,request,jsonify,render_template,redirect ,url_for ,session
# from flask_cors import CORS
# import pickle 
# import jwt
import pymongo
# import datetime
# import json
# from bson import ObjectId
# import math
# import json
from User import User

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['GestionStockage']
u1=User(username="malek",password="Pass",role="admin")
u2=User(username="chakib",password="Pass",role="admin")

db.users.insert_many([u1.__dict__,u2.__dict__])

print(u1.dict())
# print(u1.dict())
# for u in db.User.find():
#     ut=User(u)
#     print(ut.__dict__)