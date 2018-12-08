from django import template

register = template.Library()

@register.simple_tag
def replace_parameter(request, parameter, value):
    parameters = request.GET.copy()
    parameters[parameter] = value
    return parameters.urlencode()

register.filter('replace_parameter', replace_parameter)
