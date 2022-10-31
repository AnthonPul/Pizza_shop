from django.db import models
from accounts.models import User
from address.models import Address
from django.db.models import ExpressionWrapper, Sum, F
from decimal import Decimal


STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Preparing", "Preparing"),
    ("Cooking", "Cooking"),
    ("Arriving", "Arriving"),
    ("Delivered", "Delivered")
)

class OrderItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)
    startedDate = models.DateTimeField(auto_now_add=True)
    orderedDate = models.DateTimeField(blank=True, null=True)
    shippingAddress = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    payment = models.ForeignKey('Payment', null=True, blank=True, on_delete=models.DO_NOTHING)

    def getOrderTotal(self):
        total = Order.objects.get(id=self.id).items.aggregate(totalAmount=ExpressionWrapper(
            Sum(F('price') * F('quantity')), output_field=models.DecimalField()))['totalAmount']
        return round(Decimal(total), 2)

    def getItemsCount(self):
        return Order.objects.get(id=self.id).items.aggregate(quantitySum=Sum('quantity'))['quantitySum']

    def __str__(self):
        return str(self.id)

class Payment(models.Model):
    stripeChargeId = models.CharField(max_length=50)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stripeChargeId)
