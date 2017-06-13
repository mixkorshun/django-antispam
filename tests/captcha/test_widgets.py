from unittest import TestCase

from django.utils.safestring import SafeData

from antispam.captcha.widgets import ReCAPTCHA, InvisibleReCAPTCHA


class ReCAPTCHATests(TestCase):
    def setUp(self):
        self.widget = ReCAPTCHA(sitekey='mysitekey')

    def test_render_return_html(self):
        html = self.widget.render('captcha', '1234')

        self.assertIsInstance(html, SafeData)

    def test_render(self):
        html = self.widget.render('captcha', '1234')

        self.assertIn('g-recaptcha', html)

    def test_get_value_from_datadict(self):
        value = self.widget.value_from_datadict({
            'g-recaptcha-response': 'my-response'
        }, {}, 'recaptcha')

        self.assertEqual('my-response', value)


class InvisibleReCAPTCHATests(ReCAPTCHATests):
    def setUp(self):
        self.widget = InvisibleReCAPTCHA(sitekey='mysitekey')
