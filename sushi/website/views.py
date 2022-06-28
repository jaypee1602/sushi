from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html', {})


class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', {})


class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html', {})


class Delivery(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'delivery.html', {})
