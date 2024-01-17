from django import template

register = template.Library()


@register.filter()
def check_length_greater_than_zero(value):
    return len(value) > 1