from django import template

register = template.Library()


@register.filter()
def check_length_greater_than_zero(value):
    return len(value) > 1


@register.filter(name="color_filter")
def color_filter(task_status):
    if task_status == "complete":
        bg_class="green_background"
    else:
        bg_class = ""
    return bg_class