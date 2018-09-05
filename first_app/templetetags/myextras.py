from django import templete
register=template.Library()


@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')
# register.filter('cut',cut) same as @register.filter(name='cut')
