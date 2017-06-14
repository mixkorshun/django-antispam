from unittest import TestCase

from antispam.captcha.templatetags.recaptcha import recaptcha_init


class ReCAPTCHAScriptTests(TestCase):
    def test_script(self):
        script = recaptcha_init()

        self.assertIn('<script', script)
        self.assertIn('</script>', script)
