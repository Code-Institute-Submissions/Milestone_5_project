from django.apps import apps
from django.test import TestCase
from checkout.apps import CheckoutConfig


class TestAccountsConfig(TestCase):

    def test_checkout_app(self):
        self.assertEqual("checkout", CheckoutConfig.name)
        self.assertEqual("checkout", apps.get_app_config("checkout").name)
