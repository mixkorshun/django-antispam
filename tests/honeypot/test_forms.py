from unittest import TestCase

from django.core.exceptions import ValidationError

from antispam.honeypot.forms import HoneypotField


class HoneypotFieldTests(TestCase):
    def test_not_required(self):
        self.assertFalse(HoneypotField().required)

        with self.assertRaises(AssertionError):
            HoneypotField(required=False)

    def test_validate(self):
        field = HoneypotField()

        field.validate('')

        with self.assertRaises(ValidationError):
            field.validate('v')
