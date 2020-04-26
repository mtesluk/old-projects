from ..models import Topic
from django import template

register = template.Library()


@register.assignment_tag()
def most_common_topics(count=5):
    return Topic.objects.order_by('-get_count')[:count]
