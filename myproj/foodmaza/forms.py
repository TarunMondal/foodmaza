from django import forms
from foodmaza.models import Admin, Customer, Category, sub_category, Item


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class sub_categoryForm(forms.ModelForm):
    class Meta:
        model = sub_category
        fields = "__all__"


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
