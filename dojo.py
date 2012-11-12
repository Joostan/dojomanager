import cgi

from google.appengine.api import users
import webapp2
import handlers
import schema

config = {'Contact_Name': 'Tony Carden'}

applic = webapp2.WSGIApplication([
    webapp2.Route('/', handler=handlers.MainPage,name='main'),
	 webapp2.Route('/student', handler=handlers.StudentPage,name='student'),
	
     webapp2.Route('/newstudent',handler=handlers.StudentCreate,name='newstudent')
], debug=True, config=config)

