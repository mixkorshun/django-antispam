from django import forms
from django.utils.safestring import mark_safe


class ReCAPTCHA(forms.Widget):
    """
    Default reCAPTCHA v2 widget.
    (with "I'm not robot" checkbox)
    """

    def __init__(self, sitekey):
        """
        :param sitekey: site key (public key) 
        """
        super().__init__()

        self.sitekey = sitekey

    def render(self, name, value, *args, **kwargs):
        """
        Returns this widget rendered as HTML.
        """
        return mark_safe('<div class="g-recaptcha" data-sitekey="%(sitekey)s"></div>' % {
            'sitekey': self.sitekey
        })

    def value_from_datadict(self, data, files, name):
        """
        Given a dictionary of data and this widget's name, returns the value
        of this widget. Returns None if it's not provided.
        """
        return data.get('g-recaptcha-response', None)


class InvisibleReCAPTCHA(ReCAPTCHA):
    """
    Invisible reCAPTCHA widget.
    """

    def render(self, name, value, *args, **kwargs):
        """
        Returns this widget rendered as HTML.
        """

        return mark_safe(
            '<button class="g-recaptcha" data-sitekey="%(sitekey)s">%(name)s</button>' % {
                'name': name,
                'sitekey': self.sitekey
            }
        )
