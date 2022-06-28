from django.urls import path
from customer.views import Index, About, Contact, Menu, Delivery

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('menu/', Menu.as_view(), name='menu'),
    path('delivery/', Delivery.as_view(), name='delivery'),
]