from django.urls import path
from orders.views import OrderView

""" from orders.views import OrderListView, OrderFormView """

urlpatterns = [
    path('detail/', OrderView.as_view(), name='my_order'),
    path('item/', OrderView.as_view(), name='new_item'),
]
