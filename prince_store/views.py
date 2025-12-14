from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product

cart = []

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


def register_user(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('/login/')
    return render(request, 'shop/register.html')


def login_user(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'shop/login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart.append(product)
    return redirect('/cart/')


def cart_view(request):
    total = sum(p.price for p in cart)
    return render(request, 'shop/cart.html', {'cart': cart, 'total': total})


def checkout(request):
    return render(request, 'shop/checkout.html')
