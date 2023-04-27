from django import template

register = template.Library()

# @register.filter(name='stars')
# def stars(value):
#     full_stars = '⭐' * int(value)
#     empty_stars = '☆' * (5 - int(value))
#     return full_stars + empty_stars

@register.filter(name='stars')
def stars(value):
    rating_to_shape = {
        1: '★ ☆ ☆ ☆ ☆',
        2: '★ ★ ☆ ☆ ☆',
        3: '★ ★ ★ ☆ ☆',
        4: '★ ★ ★ ★ ☆',
        5: '★ ★ ★ ★ ★',
    }
    return rating_to_shape.get(int(value), '')