from unittest import TestCase, skipIf
from unittest.mock import Mock

import django
from django.utils.safestring import SafeData

from antispam.honeypot.widgets import HoneypotInput


class HoneypotInputTests(TestCase):
    def setUp(self):
        self.widget = HoneypotInput()

        # patch for support both django versions - 1.11 and 1.10
        self.widget._render = Mock(
            return_value='<input />'
        )

    def test_markup(self):
        html = self.widget.render('honeypot_field', '')
        html = str(html)

        self.assertIn('display: none;', html)

    def test_render_safe_html(self):
        html = self.widget.render('honeypot_field', '')
        self.assertIsInstance(html, SafeData)

    def test_is_hidden(self):
        self.assertTrue(self.widget.is_hidden)
