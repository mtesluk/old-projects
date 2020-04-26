from ..models import Topic
from django import template

register = template.Library()


@register.assignment_tag()
def most_common_quizes(count=5):
    return Topic.objects.order_by('-get_count')[:count]


@register.filter(name="calc_percent")
def calc_percent(num, nums):
    if nums == 0:
        return 0.00
    else:
        return round(((100 * num) / nums), 2)
