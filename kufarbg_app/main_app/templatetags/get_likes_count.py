from django import template

register = template.Library()


@register.filter
def get_likes_count(query_list, obj_id):
    return query_list.filter(trip_id=obj_id).count()
