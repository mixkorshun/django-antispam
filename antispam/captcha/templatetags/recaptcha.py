from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def recaptcha_init():
    """
    Render reCAPTCHA script tag.
    """
    url = 'https://www.google.com/recaptcha/api.js'

    return mark_safe('<script type="text/javascript" src="%s" async defer></script>' % url)
