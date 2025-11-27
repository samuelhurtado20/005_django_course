from django.urls import reverse_lazy
from django.views import generic

from products.forms import ProductForm
from products.models import Product

from .serializer import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    template_name = "products/product_list.html"
    model = Product
    context_object_name = "products"


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)