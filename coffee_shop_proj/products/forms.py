from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
    available = forms.BooleanField(
        initial=True,
        required=False,
        label="Stock",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    
    def save(self, commit=True):
        Product.objects.create(**self.cleaned_data)

    class Meta:
        model = Product
        fields = ["name", "description", "price", "image"]
