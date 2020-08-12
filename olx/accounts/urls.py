from django.urls import path
from django.contrib.auth import login

# from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', login, {'template_name': 'registration/login.html'}, name='name'),
    # path('<slug:category_slug>', views.productlist, name='product_list_category'),
    # path('detail/<slug:product_slug>', views.productdetail, name='product_detail')
]
