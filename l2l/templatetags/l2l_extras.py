from django import template

register = template.Library()
@register.filter(name='l2l_dt')

def l2l_dt(value):
    date_formatted =  ""
    if isinstance(value, str):
        date_formatted = value.replace("T"," ")
    else: 
        date_formatted = value.strftime("%Y-%m-%d %H:%M:%S")
    
    return date_formatted

 