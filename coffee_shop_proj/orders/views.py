from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderItemForm
from orders.models import Order, OrderItem


class OrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()


class CreateOrdenItemView(LoginRequiredMixin, CreateView):
    # model = OrderItem
    template_name = "orders/new_item.html"
    form_class = OrderItemForm
    # fields = ["product", "quantity"]
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        # order_item = form.save(commit=False)
        order, _ = Order.objects.get_or_create(is_active=True, user=self.request.user)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
