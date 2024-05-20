from django import forms
from .models import Receipt, Item

class ReceiptForm(forms.ModelForm):
    date_time = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Receipt
        fields = ['shop_name', 'date_time','total']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['receipt', 'product_name', 'price', 'quantity']


