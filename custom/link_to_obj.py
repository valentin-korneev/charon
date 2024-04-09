from django.urls import reverse
from django.utils.html import format_html


def link_to_obj(obj_app, obj_class, obj_id, obj_name):
    link = reverse('admin:{}_{}_change'.format(obj_app, obj_class), args=[obj_id])
    return format_html('<a href="{}">{}</a>', link, obj_name)
