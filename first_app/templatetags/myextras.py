from django import template
register=template.Library()


@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')
# register.filter('cut',cut) same as @register.filter(name='cut')

@register.filter(name='lindex')
def lindex(Lu):
    return [int(i) for i in Lu]
@register.filter(name='Justify')
def Justify(Lu,x):
    return Lu[int(x)]
@register.filter(name='str_adder')
def str_adder(pu):
    return 'images/sample/{}.jpg'.format(pu)
@register.filter(name='genre_adder')
def genre_adder(gu):
    if len(gu)==1:
        return gu[0]
    else:
        return '\n'.join(gu)
@register.filter(name='strer')
def strer(Lu):
    return [str(i) for i in Lu]
