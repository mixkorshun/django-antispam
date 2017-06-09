from unittest import TestCase
from unittest.mock import Mock

from django.http import HttpRequest

from antispam.akismet.utils import get_client_ip


class GetClientIpAddressTests(TestCase):
    def setUp(self):
        self.request = Mock(
            META={}
        )

    def test_ip_by_remote_addr(self):
        self.request.META['REMOTE_ADDR'] = '121.0.0.1'

        self.assertEqual('121.0.0.1', get_client_ip(self.request))

    def test_ip_by_x_forwarded_for(self):
        self.request.META['REMOTE_ADDR'] = '121.0.0.1'
        self.request.META['HTTP_X_FORWARDED_FOR'] = '122.0.0.1,'

        self.assertEqual('122.0.0.1', get_client_ip(self.request))

    def test_ip_by_real_ip(self):
        self.request.META['REMOTE_ADDR'] = '121.0.0.1'
        self.request.META['HTTP_X_FORWARDED_FOR'] = '122.0.0.1,'
        self.request.META['HTTP_X_REAL_IP'] = '123.0.0.1'

        self.assertEqual('123.0.0.1', get_client_ip(self.request))

    def test_no_ip_address(self):
        self.assertIsNone(get_client_ip(self.request))
