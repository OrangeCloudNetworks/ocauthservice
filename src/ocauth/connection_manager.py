'''
Created on 2012-02-20

This class is responsible for all of the connections and global connection 
variables.

@author: fransham
'''

from pymongo import Connection
import gridfs

class Constants(object):
    database = "ocsync"
    user_collection = "ocusers"
    
    
def get_collection(coll_name, database=Constants.database):
    connection = Connection()
    db = connection[database]
    return db[coll_name]

def get_user_collection():
    return get_collection(Constants.user_collection)
    
    