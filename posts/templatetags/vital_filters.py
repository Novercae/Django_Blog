from atexit import register
from django import template

register = template.Library()

@register.filter(name='comment_plural')
def comment_plural(num_comments):
    if num_comments == 1:
        v = '1 comment'
        return v   
    if num_comments == 0:
        v = 'No comments'
        return v
    else:
        v = '%s comments' % num_comments
        return v

@register.filter(name='comment_count')
def comment_count(comment):
    if comment == 1:
        v = '(1) comment'
        return v
    else:
        v = '(%s) comments' % comment
        return v