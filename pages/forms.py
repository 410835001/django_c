from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Account, User, GoodsInfo, favorite, Brand, Product, Cart
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入帳號", 'class': 'form-control'})
    )
    email = forms.EmailField(
         label=_('電子信箱'),
         widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
         error_messages={
             'invalid': '請輸入有效電子信箱',
             'required': '尚未輸入電子信箱',
         }
     )

    password1 = forms.CharField(
         label=_('密碼'),
         strip=False,
         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
         error_messages={'required': '尚未輸入密碼'},
      )
    password2 = forms.CharField(
         label=_('確認密碼'),
         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
         strip=False,
         error_messages={'required': '尚未輸入確認密碼'},
     )
    error_messages = {
         'password_mismatch': _('兩次密碼輸入不同'),
     }

    identity = ((0, '顧客'), (1, '廠商'))
    type = forms.ChoiceField(label='身份別', widget=forms.Select, choices=identity)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2', 'type')
    def clean_email(self):

        email = self.cleaned_data['email']
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'{email}已被註冊')


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入帳號", 'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"placeholder": "請輸入密碼", 'class': 'form-control'})
    )


class UpdateForm(forms.ModelForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入帳號", 'class': 'form-control'})
    )
    last_name = forms.CharField(
        label="名稱",
        widget=forms.TextInput(attrs={"placeholder": "請輸入名稱", 'class': 'form-control'})
    )
    email = forms.EmailField(
         label=_('電子信箱'),
         widget=forms.EmailInput(attrs={"placeholder": "請輸入電子信箱", 'class': 'form-control'}),
         error_messages={
             'invalid': '請輸入有效電子信箱',
             'required': '尚未輸入電子信箱',
         }
     )
    YEARS = [str(x) for x in range(1920, 2021)]
    MONTHS = {
     1: _('一月'), 2: _('二月'), 3: _('三月'), 4: _('四月'),
     5: _('五月'), 6: _('六月'), 7: _('七月'), 8: _('八月'),
     9: _('九月'), 10: _('十月'), 11: _('十一月'), 12: _('十二月')
     }
    date_of_birth = forms.DateField(
         label=_('生日'),
         widget=forms.SelectDateWidget(years=YEARS, months=MONTHS),
         error_messages={
        'invalid': '請輸入有效生日日期',
         'required': '請輸入生日',
         }
      )
    password1 = forms.CharField(
         label=_('密碼'),
         strip=False,
         widget=forms.PasswordInput(attrs={"placeholder": "請輸入密碼", 'class': 'form-control'}),
         error_messages={'required': '尚未輸入密碼'},
      )
    password2 = forms.CharField(
         label=_('確認密碼'),
         widget=forms.PasswordInput(attrs={"placeholder": "請再次輸入密碼", 'class': 'form-control'}),
         strip=False,
         error_messages={'required': '尚未輸入確認密碼'},
     )
    error_messages = {
         'password_mismatch': _('兩次密碼輸入不同'),
     }

    sex_choice = ((0, '生理女'), (1, '生理男'))

    gender = forms.ChoiceField(label='性别', widget=forms.Select, choices=sex_choice)

    phone_number=forms.CharField(
        label="電話號碼",
        widget=forms.TextInput(attrs={"placeholder": "請輸入電話號碼", 'class': 'form-control'})
    )
    class Meta:
        model = Account
        fields = ('username', 'last_name', 'email', 'date_of_birth', 'password1', 'password2', 'phone_number','gender')


class Partner_Form(forms.ModelForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入帳號", 'class': 'form-control'})
    )

    last_name = forms.CharField(
        label="名稱",
        widget=forms.TextInput(attrs={"placeholder": "請輸入名稱", 'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"placeholder": "請輸入密碼", 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={"placeholder": "請再次輸入密碼", 'class': 'form-control'})
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={"placeholder": "請輸入電子信箱", 'class': 'form-control'})
    )

    tax_ID_number = forms.CharField(
        label="統一編號",
        widget=forms.TextInput(attrs={"placeholder": "請輸入統一編號", 'class': 'form-control'})
    )
    address = forms.CharField(
        label="地址",
        widget=forms.TextInput(attrs={"placeholder": "請輸入地址", 'class': 'form-control'})
    )

    phone_number = forms.CharField(
        label="電話號碼",
        widget=forms.TextInput(attrs={"placeholder": "請輸入電話號碼", 'class': 'form-control'})
    )

    class Meta:
        model = Account
        fields = ('username', 'last_name', 'password1', 'password2', 'email',
                  'tax_ID_number', 'address','phone_number')

class GoodsInfoForm(forms.ModelForm):
    goods_name = forms.CharField(label="名稱")
    goods_price = forms.IntegerField(label="價格")
    goods_desc = forms.CharField(label="商品詳情")
    goods_img = forms.ImageField(label="圖片")
    goods_tag = forms.CharField(label="分類")
    class Meta:
        model = GoodsInfo
        fields = ('goods_name', 'goods_price', 'goods_desc', 'goods_img')

class favForm(forms.ModelForm):
    goods_name = forms.CharField(label="名稱")
    goods_price = forms.IntegerField(label="價格")
    goods_desc = forms.CharField(label="商品詳情")
    goods_img = forms.ImageField(label="圖片")
    goods_tag = forms.CharField(label="分類")

    class Meta:
        model = favorite
        fields = ('goods_name', 'goods_img')
    def clean(self):
        return self.cleaned_data

class BrandForm(forms.ModelForm):
    # 設定提示字 row顯現為1
    brand_name = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "品牌名稱",  "rows": 1}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "描述", "rows": 5}))
    email = forms.EmailField(widget=forms.Textarea(attrs={"placeholder": "連絡信箱", "rows": 1}))
    phone_number = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "聯絡電話", "rows": 1}))

    class Meta:
        model = Brand
        fields = [
            'brand_name',
            'description',
            'email',
            'phone_number'
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not (email.endswith("com") or email.endswith("tw")):
            raise forms.ValidationError("This is not a valid email")
        return email

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(label="品名", widget=forms.Textarea(attrs={"placeholder": "請輸入品名", "rows": 1}))
    # brand = forms.MultipleChoiceField(queryset=None)
    material_color = forms.CharField(label="材質及配色", required=False, widget=forms.Textarea(attrs={"placeholder": "概要", "rows": 1}))
    description = forms.CharField(label="描述", widget=forms.Textarea(attrs={"placeholder": "描述", "rows": 3}))
    price = forms.DecimalField(label="價格", initial=0.0)
    # picture = forms.ImageField(label="商品圖片", required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # threeD_model = forms.FileField(label="商品3D模型", required=False)

    class Meta:
        model = Product
        fields = [
            'brand',
            'product_name',
            'material_color',
            'description',
            'price',
            'picture',
            'threeD_model'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("product_name")
        if "asd" in title:
            raise forms.ValidationError("This is not a valid title")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "品名", "rows": 1}))
    description = forms.CharField( widget=forms.Textarea(attrs={"placeholder": "描述", "rows": 5}))
    summary = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "概要", "rows": 5}))
    price = forms.DecimalField(initial=0.0)

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['account', 'product']