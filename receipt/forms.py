from django import forms
from .models import Receipt, Item
from django.contrib.admin.widgets import AdminDateWidget

class ReceiptForm(forms.ModelForm):
    date_time = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Receipt
        fields = ['shop_name', 'date_time','total']

class ItemForm(forms.ModelForm):
    expiration_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Item
        fields = ['receipt', 'product_name', 'price', 'quantity', 'expiration_date']
