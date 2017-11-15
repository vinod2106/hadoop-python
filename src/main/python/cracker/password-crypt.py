'''
Created on 12 Nov 2017

@author: vinsharm
'''
#import crypt as c
#print(c.crypt("nxsyed","NX"))
import bcrypt
#salt = uuid.uuid4().hex
#hashed_password = hashlib.md5("nxsyed"+"NX").digest
hashed_password = bcrypt.hashpw("nxsyed",bcrypt.gensalt())
print hashed_password