from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('cart/checkout/', views.checkout, name="checkout"),
    path('detail/<int:id>/', views.detail_view, name="detail"),
    path('wish-list/', views.wish_list, name="wish-list"),


    path('store/process_order/', views.processOrder, name="process_order"),

    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),

]
