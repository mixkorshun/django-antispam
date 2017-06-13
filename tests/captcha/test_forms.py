from unittest import TestCase

from antispam.captcha import widgets
from antispam.captcha.forms import ReCAPTCHA


class ReCAPTCHATests(TestCase):
    def setUp(self):
        self.field = ReCAPTCHA(
            sitekey='my-sitekey',
            secretkey='my-secretkey',
            timeout=3,
            pass_on_error=False,
            widget=widgets.ReCAPTCHA,
        )

    def test_field_defaults(self):
        pass

    def test_recaptcha_server_connection_timeout(self):
        pass

    def test_recaptcha_validation_ok(self):
        pass

    def test_recaptcha_validation_failed(self):
        pass

    def test_recaptcha_validation_unexpected_error(self):
        pass

    def test_recaptcha_pass_on_error(self):
        pass
