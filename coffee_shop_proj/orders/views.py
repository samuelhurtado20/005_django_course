from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order, OrderItem


class OrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()


class CreateOrdenItemView(LoginRequiredMixin, CreateView):
    model = OrderItem
    template_name = "orders/new_item.html"
    fields = ["product", "quantity"]
    success_url = reverse_lazy("orders:order")
