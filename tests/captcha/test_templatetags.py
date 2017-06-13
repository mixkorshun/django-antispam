from unittest import TestCase

from antispam.captcha.templatetags.recaptcha import recaptcha_script


class ReCAPTCHAScriptTests(TestCase):
    def test_script(self):
        script = recaptcha_script()

        self.assertIn('<script', script)
        self.assertIn('</script>', script)
