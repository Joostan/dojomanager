import webapp2
import cgi
import logging
from google.appengine.ext import db
import schema

import jinja2
import os

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class origMainPage(webapp2.RequestHandler):
    def get(self):
		self.response.out.write("""
			<html>
			<body>
			<form action="/sign" method="post">
			<div><textarea name="content" rows="3" cols="60" >"""+self.request.get('getval')+"""</textarea></div>
			<div><input name="iamawesome" value="WHOOO"></div>
			<div><input type="submit" value="Sign Guestbook"></div>
			</form>""")
		self.response.out.write('<br/>'+self.request.get('getval'))
		uri = webapp2.uri_for('student', _full=True)
		self.response.out.write('<br/><a href="'+uri+'">A link to the students page</a>')
		self.response.out.write('</body> </html>')
		
class MainPage(webapp2.RequestHandler):
    def get(self):		
		template = jinja_environment.get_template('templates/dojohome.html')
		self.response.out.write(template.render())
         

class StudentCreate(webapp2.RequestHandler):
	def post(self):
		logging.info('entry point')
		logging.info(self.request.get('studentfirstname'))
		if self.request.get('delKey'):
		    if self.request.get('delStudent'):
			    existing = schema.Student.get(cgi.escape(self.request.get('delKey')))
			    existing.delete()
			    self.redirect("/student")
			
		
		elif self.request.get('updateKey'):
			existing = schema.Student.get(cgi.escape(self.request.get('updateKey')))
			if existing.is_saved():
				existing.firstname=cgi.escape(self.request.get('studentfirstname'))
				if self.request.get('studentlastname'):
				  existing.lastname=cgi.escape(self.request.get('studentlastname'))
				if self.request.get('studentphone'):
				  existing.phone=cgi.escape(self.request.get('studentphone'))
				if self.request.get('studentemail'):				
				  existing.email=cgi.escape(self.request.get('studentemail'))
				if self.request.get('studentaddress'):
				  existing.address=cgi.escape(self.request.get('studentaddress'))
				if self.request.get('studentmonbid'):
				  existing.monbid=cgi.escape(self.request.get('studentmonbid'))
				if self.request.get('studentedgeid'):
				  existing.edgeid=cgi.escape(self.request.get('studentedgeid'))
				if self.request.get('studentmembexp'):
				  existing.membexp=cgi.escape(self.request.get('studentmembexp'))
				if self.request.get('studenttuitexp'):
				  existing.tuitexp=cgi.escape(self.request.get('studenttuitexp'))
				if self.request.get('studentnotes'):
				  existing.notes=cgi.escape(self.request.get('studentnotes'))
				logging.info('variable filled')
				existing.put()
				self.redirect("/student")
		else:
			try:
				a = schema.Student(
					firstname=cgi.escape(self.request.get('studentfirstname')),
					lastname=cgi.escape(self.request.get('studentlastname')),
					phone=cgi.escape(self.request.get('studentphone')),
					email=cgi.escape(self.request.get('studentemail')),
					address=cgi.escape(self.request.get('studentaddress')),
					monbid=cgi.escape(self.request.get('studentmonbid')),
					edgeid=cgi.escape(self.request.get('studentedgeid')),
					membexp=cgi.escape(self.request.get('studentmembexp')),
					tuitexp=cgi.escape(self.request.get('studenttuitexp')),
					notes=cgi.escape(self.request.get('studentnotes')))
				logging.info('variable filled')
				a.put()
				logging.info('put')
				self.redirect("/student")
			except:
				logging.info('hola')	
		self.response.out.write('<html><body>Student Create:<pre>')
		self.response.out.write('<p class="error">There seemed to be an error with that post! care to try again?</p>')
		self.response.out.write(cgi.escape(self.request.get('studentfirstname')))
		self.response.out.write(cgi.escape(self.request.get('studentlastname')))
		self.response.out.write(cgi.escape(self.request.get('studentphone')))
		self.response.out.write(cgi.escape(self.request.get('studentemail')))
		self.response.out.write(cgi.escape(self.request.get('studentaddress')))
		self.response.out.write(cgi.escape(self.request.get('studentmonbid')))
		self.response.out.write(cgi.escape(self.request.get('studentedgeid')))
		self.response.out.write(cgi.escape(self.request.get('studentmembexp')))
		self.response.out.write(cgi.escape(self.request.get('studenttuitexp')))
		self.response.out.write(cgi.escape(self.request.get('studentnotes')))
		self.response.out.write(cgi.escape(self.request.get('updateKey')))
		self.response.out.write('</pre>')
		uri = webapp2.uri_for('student', _full=True, getval=self.request.get('content'))
		self.response.out.write('<a href ="')
		self.response.out.write(uri)
		self.response.out.write('">Student Listings</a>')
		foo = self.app.config.get('Contact_Name')
		self.response.write('<br/>Main contact is %s' % foo)
		self.response.out.write('</body></html>')
		logging.debug("value of my var is %s", str(uri))	


		
				
class StudentPage(webapp2.RequestHandler):
    def get(self):
		
		template_values = {
			'studentQ': schema.Student.all(),
			'headings': ['First Name', 'Last Name', 'Phone', 'Email', 'Address', 'MonbID', 'EdgeID', 'MembExp', 'TuitExp', 'Notes', 'Edit', 'Del']
			}
		template = jinja_environment.get_template('templates/students.html')
		self.response.out.write(template.render(template_values))