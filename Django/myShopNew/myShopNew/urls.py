"""myShopNew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from user import views as UserViews
from product import views as ProductViews


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),


    path('login/', UserViews.login_form, name='login'),
    path('signup/', UserViews.signup, name='signup'),
    path('logout/', UserViews.logout_func, name='logout'),
    path('user/', include('user.urls')),

    path('product/<int:id>/<slug:slug>/',
         ProductViews.product_detail, name='product_detail'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ajaxcolor/', ProductViews.ajaxcolor, name='ajaxcolor'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
