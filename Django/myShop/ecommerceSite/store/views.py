from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
import datetime

from .models import *

from .forms import CreateUserForm

from .utils import cookieCart, cartData, wishListData, guestOrder

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator


# Create your views here.


def index(request):
    data = cartData(request)
    cartItems = data['cartItems']

    wish_list_data = wishListData(request)
    wishListTotal = wish_list_data['wishListTotal']

    context = {'cartItems': cartItems, 'wishListTotal': wishListTotal}
    return render(request, 'index.html', context)


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    wish_list_data = wishListData(request)
    wishListTotal = wish_list_data['wishListTotal']

    productsFilterOne = Product.objects.filter(
        continue_selling_when_out_of_stock=True)
    productsFilterTwo = Product.objects.filter(
        stock_keeping_unit__gt=0, continue_selling_when_out_of_stock=False)
    products = productsFilterOne | productsFilterTwo

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {'products': products,
               'cartItems': cartItems, 'wishListTotal': wishListTotal}
    return render(request, 'store.html', context)


def detail_view(request, id):
    data = cartData(request)
    cartItems = data['cartItems']

    wish_list_data = wishListData(request)
    wishListTotal = wish_list_data['wishListTotal']

    productsFilterOne = Product.objects.filter(
        continue_selling_when_out_of_stock=True)
    productsFilterTwo = Product.objects.filter(
        stock_keeping_unit__gt=0, continue_selling_when_out_of_stock=False)
    products = productsFilterOne | productsFilterTwo

    product = get_object_or_404(products, id=id)
    productPhotos = ProductImage.objects.filter(product=product)

    context = {'product': product, 'productPhotos': productPhotos,
               'cartItems': cartItems, 'wishListTotal': wishListTotal}
    return render(request, 'detail.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    cartTotal = data['cartTotal']
    items = data['items']

    wish_list_data = wishListData(request)
    wishListTotal = wish_list_data['wishListTotal']

    context = {'items': items, 'cartTotal': cartTotal,
               'cartItems': cartItems, 'wishListTotal': wishListTotal}
    return render(request, 'cart.html', context)


def wish_list(request):
    data = cartData(request)
    cartItems = data['cartItems']
    cartTotal = data['cartTotal']
    items = data['items']

    wish_list_data = wishListData(request)
    wishListItems = wish_list_data['wishListItems']
    wishListTotal = wish_list_data['wishListTotal']

    context = {'items': items, 'cartTotal': cartTotal,
               'cartItems': cartItems, 'wishListItems': wishListItems, 'wishListTotal': wishListTotal}
    return render(request, 'wishlist.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    cartTotal = data['cartTotal']
    items = data['items']

    wish_list_data = wishListData(request)
    wishListTotal = wish_list_data['wishListTotal']

    context = {'items': items, 'cartTotal': cartTotal,
               'cartItems': cartItems,  'wishListTotal': wishListTotal}

    if cartTotal == 0:
        return redirect('cart')
    else:
        return render(request, 'checkout.html', context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = data['form']['total']
    order.transaction_id = transaction_id

    if int(total) == int(order.get_cart_total):
        order.complete = True

    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode']
    )

    return JsonResponse("Order Processed...", safe=False)


def login(request):
    if request.user.is_authenticated:
        return redirect('store')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('store')
            else:
                messages.info(request, 'Username or Password is not correct!')

        return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('store')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('index')
