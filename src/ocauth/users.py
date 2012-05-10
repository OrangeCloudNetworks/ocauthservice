'''
Created on 2012-02-20

@author: fransham
'''

import connection_manager
from M2Crypto import RSA
from twisted.conch.ssh import keys

class UserRepo(object):
    '''
    Manages users for the Orange Cloud Secure File Repository
    '''
        
    def add_user(self, username, password):
        
        # Generate an ssh keypair for the user
        ssh_private = RSA.gen_key(1024, 65337).as_pem(cipher=None)
        twisted_key = keys.RSA.importKey(ssh_private)
        ssh_public = keys.Key(twisted_key).public().toString("openssh")  
        
        #add the user to the db.  
        user = {"username": username,
                "password": password,
                "pub_key": ssh_public,
                "priv_key": ssh_private}
        return connection_manager.get_user_collection().insert(user)
    
    def get_user(self, username, password):
        user = connection_manager.get_user_collection().find_one({"username":username,
                                                                  "password":password})
        return user
    
    def remove_user(self, username):
        connection_manager.get_user_collection().remove({"username":username})
  
    def update_password(self, username, password):
        connection_manager.get_user_collection().update({"username":username},
                                                          {"$set": {"password": password}}, 
                                                           multi=False)