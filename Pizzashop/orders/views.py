from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from menu.models import (RegularPizza, SicilianPizza, Extra, Pasta, 
                         Platter, Sub, Salad, Topping)

class CartListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(template_name="orders/cart.html")

class OrderListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        context = {
            "toppings": Topping.objects.all().order_by('name'),
            "reg_pizza": RegularPizza.objects.all(),
            "sic_pizza": SicilianPizza.objects.all(),
            "pastas": Pasta.objects.all(),
            "salads": Salad.objects.all(),
            "platters": Platter.objects.all(),
            "subs": Sub.objects.all(),
            "extras": Extra.objects.all()
        }
        return Response(data=context, template_name="orders/order_place.html")