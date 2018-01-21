from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .widgets import HoneypotInput


class HoneypotField(forms.CharField):
    """
    Honeypot form field.
    """
    default_error_messages = {
        'invalid': _('Enter a number.'),
        'honeypot': _('Invalid value for honey pot field.'),
    }

    def __init__(self, **kwargs):
        assert 'required' not in kwargs
        kwargs['required'] = False

        kwargs.setdefault('max_length', 255)
        kwargs.setdefault('widget', HoneypotInput)

        super(HoneypotField, self).__init__(**kwargs)

    def validate(self, value):
        """
        Validates form field value entered by user.

        :param value: user-input
        :raise: ValidationError with code="spam-protection"
                if honeypot check failed.
        """
        super(HoneypotField, self).validate(value)

        if value:
            raise ValidationError(self.error_messages['honeypot'],
                                  code='spam-protection')
