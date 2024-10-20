from django import template

register=template.Library()

@register.simple_tag()
def get_halfContent(idea_description):
    return idea_description[:int(len(idea_description)/5)]
