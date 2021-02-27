import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    cartItems = 0
    cartTotal = 0

    for i in cart:
        try:
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            cartItems += cart[i]['quantity']
            cartTotal += total

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)
        except:
            pass

    return {'cartItems': cartItems, 'cartTotal': cartTotal, 'items': items}


def cartData(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    cartTotal = cookieData['cartTotal']
    items = cookieData['items']

    return {'cartItems': cartItems, 'cartTotal': cartTotal, 'items': items}


def cookieWishList(request):
    try:
        wishList = json.loads(request.COOKIES['wish_list'])
    except:
        wishList = []
    items = []
    wishListTotal = 0

    for i in wishList:
        try:
            product = Product.objects.get(id=i)

            wishListTotal += 1

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
            }
            items.append(item)
        except:
            pass

    return {'wishListItems': items, 'wishListTotal': wishListTotal}


def wishListData(request):
    cookieData = cookieWishList(request)
    wishListItems = cookieData['wishListItems']
    wishListTotal = cookieData['wishListTotal']

    return {'wishListItems': wishListItems, 'wishListTotal': wishListTotal}


def guestOrder(request, data):
    print("User is not Logged In..")
    print("COOKIE", request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        name=name, email=email)

    order = Order.objects.create(
        customer=customer, complete=False)

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product=product, order=order, quantity=item['quantity'])

    return customer, order
