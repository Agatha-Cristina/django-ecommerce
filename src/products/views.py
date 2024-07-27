from django.view.generic import ListView
from django.shortcuts import render


from .models import Product

class ProductListView(ListView):
    queryset = Produc.objects.all()
    template_name = "products/list.html"
# Create your views here.

def product_list_view(request):
    queryset = Product.objects.all()
    conexr = {
        'qs': queryset
    }
return render(request, "products/list.html", context)