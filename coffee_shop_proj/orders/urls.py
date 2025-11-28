from django.urls import path
from orders.views import CreateOrdenItemView, OrderView

""" from orders.views import OrderListView, OrderFormView """

urlpatterns = [
    path("detail/", OrderView.as_view(), name="my_order"),
    path("item/", CreateOrdenItemView.as_view(), name="add_item"),
]
