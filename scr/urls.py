"""scr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from pages.views import home_view, contact_view, sign_in, logout_view, login_view, text_view, car_view, order_view,\
material, listall, delete, about, collect, us, detail, Brand_list_view, Brand_create_view, Brand_detail_view, Brand_update_view, Brand_delete_view, navbar, threed_model_view,\
product_list_view, product_create_view, product_detail_view, product_update_view,product_delete_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contact_view),
    path('sign/', sign_in),
    path('login/', login_view),
    path('logout/', logout_view),
    path('profile/', home_view),
    path('text/', text_view),
    path('car/', car_view),
    path('order/', order_view),
    path('material/', material),
    path('listall/', listall),
    path('delete/', delete),
    path('about/', about),
    path('collect/', collect),
    path('us/', us),
    path('detail/<int:id>/', detail, name='detail'),
    path('list/', Brand_list_view),
    path('create/', Brand_create_view),
    path('Brand/<int:b_id>/', Brand_detail_view, name='Brand-detail'),
    path('Brand/<int:b_id>/update/', Brand_update_view, name='Brand-update'),
    path('Brand/<int:b_id>/delete/', Brand_delete_view, name='Brand-delete'),
    path('3D_js/', threed_model_view),
    path('products/', product_list_view, name='product-list'),
    path('product_create/', product_create_view, name='product-list'),
    path('product/<int:p_id>/', product_detail_view, name='product-detail'),
    path('product/<int:p_id>/update/', product_update_view, name='product-update'),
    path('product/<int:p_id>/delete/', product_delete_view, name='product-delete'),
    path('admin/', admin.site.urls),
]+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
