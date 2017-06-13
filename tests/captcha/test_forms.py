import json
from unittest import TestCase
from unittest.mock import patch

from django.core.exceptions import ValidationError
from requests import ConnectionError, Response

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

    def _get_response(self, json_data):
        resp = Response()
        resp.status_code = 200
        resp._content = json.dumps(json_data).encode('utf-8')
        return resp

    @patch('antispam.captcha.forms.settings')
    def test_field_defaults(self, settings):
        settings.RECAPTCHA_SITEKEY = 'sitekey-from-settings'
        settings.RECAPTCHA_SECRETKEY = 'secretkey-from-settings'
        settings.RECAPTCHA_WIDGET = 'antispam.captcha.widgets.InvisibleReCAPTCHA'
        settings.RECAPTCHA_TIMEOUT = 15
        settings.RECAPTCHA_PASS_ON_ERROR = True

        field = ReCAPTCHA()

        self.assertEqual('sitekey-from-settings', field.sitekey)
        self.assertEqual('secretkey-from-settings', field.secretkey)

        self.assertIsInstance(field.widget, widgets.InvisibleReCAPTCHA)
        self.assertEqual(field.sitekey, field.widget.sitekey)

        self.assertEqual(15, field.timeout)
        self.assertEqual(True, field.pass_on_error)

    @patch('antispam.captcha.forms.requests')
    def test_recaptcha_server_connection_error(self, requests):
        requests.post.side_effect = ConnectionError()

        with self.assertRaises(ValidationError) as e:
            self.field.validate('1234')

        self.assertEqual('captcha-error', e.exception.code)

    @patch('antispam.captcha.forms.requests')
    def test_recaptcha_internal_server_error(self, requests):
        resp = self._get_response({})
        resp.status_code = 500
        requests.post.return_value = resp

        with self.assertRaises(ValidationError) as e:
            self.field.validate('1234')

        self.assertEqual('captcha-error', e.exception.code)

    @patch('antispam.captcha.forms.requests')
    def test_recaptcha_validation_ok(self, requests):
        requests.post.return_value = self._get_response({'success': True})

        self.field.validate('1234')
        self.assertTrue(True)

    @patch('antispam.captcha.forms.requests')
    def test_recaptcha_validation_failed(self, requests):
        requests.post.return_value = self._get_response({'success': False, 'error-codes': ['invalid-input-response']})

        with self.assertRaises(ValidationError) as e:
            self.field.validate('1234')

        self.assertEqual('captcha-invalid', e.exception.code)

    @patch('antispam.captcha.forms.requests')
    def test_recaptcha_validation_unexpected_error(self, requests):
        requests.post.return_value = self._get_response({'success': False, 'error-codes': ['bad-request']})

        with self.assertRaises(ValidationError) as e:
            self.field.validate('1234')

        self.assertEqual('captcha-error', e.exception.code)

    @patch('antispam.captcha.forms.requests')
    def test_recaptcha_pass_on_error_request_error(self, requests):
        self.field.pass_on_error = True

        requests.post.side_effect = ConnectionError()

        self.field.validate('1234')
        self.assertTrue(True)

    @patch('antispam.captcha.forms.requests')
    def test_recaptcha_pass_on_error_unexpected_error(self, requests):
        self.field.pass_on_error = True

        requests.post.return_value = self._get_response({'success': False, 'error-codes': ['bad-request']})

        self.field.validate('1234')
        self.assertTrue(True)
