'''
Created on 2012-02-23

Installation script for the orange cloud sync service.  Run with 

python setup.py install

Requires cherrypy and mongodb. 

@author: fransham
'''
from distutils.core import setup

setup(name='Orange Cloud Auth Service',
      version='1.0',
      description='Manages a User authentication database',
      author='Orange Cloud Networks',
      author_email='info@orangecloud.ca',
      url='http://www.orangecloud.ca',
      package_dir = {'': 'src'},
      packages = ['ocauth'],
      scripts=['scripts/ocauthserv', 'scripts/ocauthservd']
      data_files=[('/etc/init.d', ['scripts/ocauth'])]
     )
