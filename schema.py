import datetime
from google.appengine.ext import db
from google.appengine.api import users
import logging

#logging.info('this is a random message')
class Student(db.Model):
	firstname =  db.StringProperty(required=True)
	lastname = db.StringProperty()
	phone = db.StringProperty()
	email = db.StringProperty()
	address = db.StringProperty()
	monbid = db.StringProperty()
	edgeid = db.StringProperty()
	membexp = db.StringProperty()
	tuitexp = db.StringProperty()
	notes = db.StringProperty()
