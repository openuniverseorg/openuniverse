from django import template
from datetime import datetime
register = template.Library()

#This template tag takes an string, converts it to a datetime objet and then return the year of its timestamp
@register.filter(name='duration')
def duration(value):
	return datetime.now().year - datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').year
	
	