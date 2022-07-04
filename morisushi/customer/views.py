from django.shortcuts import render
from django.views import View
from .models import MenuItem, OrderModel, Category
from cart.forms import CartAddProductForm


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html', {})


class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', {})


class Menu(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        uramaki = MenuItem.objects.filter(category__name__contains='uramaki')
        nigiri = MenuItem.objects.filter(category__name__contains='nigiri')
        hosomaki = MenuItem.objects.filter(category__name__contains='hosomaki')
        temaki = MenuItem.objects.filter(category__name__contains='temaki')

        # pass into context
        context = {'uramaki': uramaki,
                   'nigiri': nigiri,
                   'hosomaki': hosomaki,
                   'temaki': temaki,
                   }
        return render(request, 'menu.html', context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }
        return render(request, 'orderconfirmation.html', context)


class Delivery(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'delivery.html', {})


class Cart(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = MenuItem.objects.get_or_create(customer)
        return render(request, 'cart.html', {})
