from django.urls import include, path
from .views import home, dashboard, Products,qrcode,sales,customers,sendNotification


urlpatterns = [
    path('', home, name='Home'),
    path('dashboard/', dashboard, name='Dashboard'),
    path('products/',Products, name='Products'),
    path('qrcode/',qrcode, name='qrcode'),
    path('sales/',sales, name='Sales'),
    path('customers/',customers, name='Customers'),
    path('notifications/',sendNotification, name='Notifications'),
]
