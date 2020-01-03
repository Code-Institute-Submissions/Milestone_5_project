from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User



class TestCartView(TestCase):
    
    def test_view_cart_page(self):
        response = self.client.get('/cart/view_cart/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
        
    def test_add_to_cart(self):
        response = self.client.get('/cart/<int:2>/add_to_cart')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')   
    
