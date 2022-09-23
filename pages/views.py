from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import RegisterForm, GoodsInfoForm, favForm, BrandForm, Partner_Form, ProductForm, CartForm
from .forms import UpdateForm
from .models import GoodsInfo, favorite, Brand, Product, Cart
from .models import User
from django.views.generic.base import View
from django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    queryset = Product.objects.all()  # list of objects
    context = {
        "object_list": queryset,
        "times": 0
    }
    return render(request, "home.html", context)

def Brand_create_view(request):
    if request.method == 'POST':
        form = BrandForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account = request.user
            instance.save()
            return redirect('/list/')
            # form.save()
            # form = PartnerForm()
        context = {
            'state': "新增品牌",
            'form': form
        }
    else:
        form = BrandForm()
        context = {
            'state': "新增品牌",
            'form': form
        }
    return render(request, "create.html", context)

def Brand_list_view(request):
    queryset = Brand.objects.all()  # list of objects
    context = {
        "object_list": queryset,
    }
    return render(request, "list.html", context)

def navbar(request, *args, **kwargs):
    home_form = GoodsInfoForm()
    products = GoodsInfo.objects.all()
    return render(request, "navbar.html", locals())

def threed_model_view(request):
    return render(request, "3D_js.html")

def contact_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, "contact.html", context)


def sign_in(request, *args, **kwargs):

    return render(request, "sign.html")

def logout_view(request):
    auth.logout(request)
    return redirect('/home/')

def login_view(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect('../sign/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('../sign/')
    else:
        return render(request, 'login.html', locals())

def text_view(request):
    user = request.user
    if user.type == 0:
        form = UpdateForm(request.POST or None, instance=user)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('/listall/')

        context = {'state': "更新資料",
                   'form': form}
    if user.type == 1:
        form1 = Partner_Form(request.POST or None, instance=user)
        if request.method == "POST":
            if form1.is_valid():
                form1.save()
                return redirect('/listall/')

        context = {'state': "更新資料",
                   'form': form1}

    return render(request, "text.html", context)

def car_view(request, *args, **kwargs):

    return render(request, "car.html")

def order_view(request, *args, **kwargs):

    return render(request, "order.html")

def material(request,*args, **kwargs):


    return render(request, "material.html")

def listall(request, *args, **kwargs):
    user = request.user
    form = UpdateForm(request.POST or None, instance=user)
    messages.warning(request, '注意！您登出前請先妥善存檔')
    return render(request, "listall.html", locals())

def delete(request, *args, **kwargs):
    goods = GoodsInfo.objects.get(id=id)
    goods.delete()
    return render(request, "collect.html", locals())

def about(request, *args, **kwargs):

    return render(request, "about.html")

def collect(request, id, *args, **kwargs):

    form = favForm()

    return render(request, "collect.html", {'form': form})

def us(request, *args, **kwargs):

    return render(request, "us.html")

def detail(request, id, *args, **kwargs):
    products = GoodsInfo.objects.all()
    goods = GoodsInfo.objects.get(id=id)

    return render(request, "detail.html", {'goods': goods,
                                           'products': products})


def Brand_delete_view(request, b_id):
    obj = get_object_or_404(Brand, id=b_id)
    if request.method == "POST":
        obj.delete()
        return redirect('/list/')
    context = {
        "object": obj
    }
    return render(request, "partner_delete.html", context)


def Brand_update_view(request, b_id):
    obj = get_object_or_404(Brand, id=b_id)
    form = BrandForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('..//../')
    context = {
        'state': "更新夥伴",
        'form': form
    }
    return render(request, "create.html", context)

def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "product_list.html", context)


def product_delete_view(request, p_id):
    obj = get_object_or_404(Product, id=p_id)
    if request.method == "POST":
        obj.delete()
        return redirect('..//../')
    context = {
        "object": obj
    }
    return render(request, "product_delete.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/products/')
    context = {
        'state': "新增品牌",
        'form': form
    }
    return render(request, "product_create.html", context)


def product_detail_view(request, p_id):
    obj = Product.objects.get(id=p_id)
    form = CartForm(request.POST or None)
    if form.is_valid():  # 我的最愛
        instance = form.save(commit=False)
        instance.account = request.user
        instance.product = obj
        instance.save()

    context = {
        'form': form,
        'object': obj
    }
    return render(request, "product_detail.html", context)


def product_update_view(request, p_id):
    obj = get_object_or_404(Product, id=p_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'state': "更新品牌",
        'form': form
    }
    return render(request, "product_create.html", context)

def Brand_detail_view(request, b_id):
    # obj = Brand.objects.get(id=b_id)
    obj = get_object_or_404(Brand, id=b_id)
    context = {
        'object': obj
    }
    return render(request, "partner_detail.html", context)
