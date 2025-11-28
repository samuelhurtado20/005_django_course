from django.forms import ModelForm
from .models import OrderItem


class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ["product"]
        # widgets = {
        #     'product': forms.Select(attrs={'class': 'form-control'}),
        #     'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        # }
