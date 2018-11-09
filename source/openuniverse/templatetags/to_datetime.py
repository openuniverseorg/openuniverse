from django import template
from datetime import datetime
from babel.dates import format_date
register = template.Library()

@register.filter(name='to_datetime')
def to_datetime(value):
	x = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').date()
	return format_date(x, locale='en')
	