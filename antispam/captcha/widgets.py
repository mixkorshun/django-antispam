from django import forms
from django.utils.safestring import mark_safe


class ReCAPTCHA(forms.Widget):
    def __init__(self, sitekey):
        super().__init__()

        self.sitekey = sitekey

    def render(self, name, value, *args, **kwargs):
        return mark_safe('<div class="g-recaptcha" data-sitekey="%(sitekey)s"></div>' % {
            'sitekey': self.sitekey
        })

    def value_from_datadict(self, data, files, name):
        return data.get('g-recaptcha-response', None)


class InvisibleReCAPTCHA(ReCAPTCHA):
    def render(self, name, value, *args, **kwargs):
        return mark_safe(
            '<button class="g-recaptcha" data-sitekey="%(sitekey)s">%(name)s</button>' % {
                'name': name,
                'sitekey': self.sitekey
            }
        )
