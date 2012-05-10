'''
Created on 2012-05-09

@author: fransham
'''

import cherrypy
from users import UserRepo

class Root(object):
    '''
    This class manages authentication for users to the Orange Cloud 
    File Repository.  
    '''

    @cherrypy.tools.allow(methods=['GET'])
    @cherrypy.expose    
    @cherrypy.tools.json_out()
    def get_authentication(self, username, password):        
        user = UserRepo().get_user(username, password)
        if user is None:
            return dict({"success": False})
        return dict({"success": True,
                     "pubkey": user.pub_key,
                     "privkey": user.priv_key})
        
        