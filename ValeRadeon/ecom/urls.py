from django.contrib import admin
from django.urls import path

from accounts.views import login_user, logout_user, signup
from ecom import settings
from store.views import add_to_cart, cart, checkout, confirmation, delete_cart, index, product_details
from django.conf.urls.static import static

urlpatterns = [
    path('' , index ,name='index'),
    path('home/' , index ,name='index'),
    path('admin/', admin.site.urls),
    path('signup/' , signup ,name='signup'),
    path('logout/' , logout_user ,name='logout_user'),
    path('login/' , login_user ,name='login_user'),
    path('cart/' , cart ,name='cart'),
    path('cart/checkout' , checkout ,name='checkout'),
    path('cart/checkout/confirmation' , confirmation ,name='confirmation'),
    path('cart/delete' , delete_cart ,name='delete_cart'),
    path('product/<str:slug>', product_details, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add_to_cart"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
