import requests
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _

from . import default_settings


class ReCAPTCHA(forms.Field):
    """
    reCAPTCHA form field.
    
    Only single field on page can be shown.
    """
    default_error_messages = {
        'connection-error': _('Connection to reCAPTCHA server failed.'),
        'invalid': _('reCAPTCHA invalid or expired. Please try again'),
        'bad-request': _('reCAPTCHA cannot be checked due configuration problem.'),
    }

    def __init__(self, sitekey=None, secretkey=None, timeout=None, pass_on_error=None, **kwargs):
        """
        :param sitekey: site key (public)
        :param secretkey: secret key (private)
        :param timeout: connection to recaptcha service timeout
        :param pass_on_error: do not raise exception if recaptcha service is not working.
        """
        self.sitekey = sitekey or getattr(settings, 'RECAPTCHA_SITEKEY')
        self.secretkey = secretkey or getattr(settings, 'RECAPTCHA_SECRETKEY')

        if timeout is None:
            timeout = getattr(settings, 'RECAPTCHA_TIMEOUT', default_settings.RECAPTCHA_TIMEOUT)
        self.timeout = timeout

        if pass_on_error is None:
            pass_on_error = getattr(settings, 'RECAPTCHA_PASS_ON_ERROR', default_settings.RECAPTCHA_PASS_ON_ERROR)
        self.pass_on_error = pass_on_error

        if not 'widget' in kwargs:
            recaptcha_widget = import_string(getattr(settings, 'RECAPTCHA_WIDGET', default_settings.RECAPTCHA_WIDGET))
            kwargs['widget'] = recaptcha_widget(sitekey=self.sitekey)
        elif isinstance(kwargs['widget'], type):
            kwargs['widget'] = kwargs['widget'](sitekey=self.sitekey)

        super().__init__(**kwargs)

    def validate(self, value):
        """
        Validate reCAPTCHA value.
        
        :raise ValidationError with code="captcha-error" if reCAPTCHA service is unavailable or working incorrectly.
        :raise ValidationError with code="captcha-invalid" if reCAPTCHA validation failed.
        """
        super().validate(value)

        try:
            resp = requests.post('https://www.google.com/recaptcha/api/siteverify', {
                'secret': self.secretkey,
                'response': value
            }, timeout=self.timeout)

            resp.raise_for_status()
        except IOError:
            if self.pass_on_error:
                return

            raise ValidationError(self.error_messages['connection-error'], code='captcha-error')

        resp = resp.json()

        if not resp['success']:
            if 'missing-input-response' in resp['error-codes'] or 'invalid-input-response' in resp['error-codes']:
                raise ValidationError(self.error_messages['invalid'], code='captcha-invalid')
            else:
                if self.pass_on_error:
                    return

                raise ValidationError(self.error_messages['bad-request'], code='captcha-error')
