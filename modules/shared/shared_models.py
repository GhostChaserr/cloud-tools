from peewee import Model, CharField
from db.conn import db

class Activity(Model):
  
  # Table Columns
  path_name = CharField(max_length=255)
  operation = CharField(max_length=255)
  user_agent = CharField(max_length=255)

  class Meta:
    database = db 