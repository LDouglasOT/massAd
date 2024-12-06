from django.shortcuts import render


def home(request):
    return render(request, 'whatsapp/homepage.html')

def dashboard(request):
    return render(request, 'whatsapp/dashboard.html')


def Products(request):
    return render(request, 'whatsapp/products.html')

def qrcode(request):
    return render(request, 'whatsapp/qrcode.html')

def sales(request):
    return render(request, 'whatsapp/sales.html')

def customers(request):
    return render(request, 'whatsapp/customers.html')

def sendNotification(request):
    return render(request, 'whatsapp/notifications.html')    