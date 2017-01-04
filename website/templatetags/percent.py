from django import template
register=template.Library()

@register.filter

def percent(value):
    return value+"%"

