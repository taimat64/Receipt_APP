from django.urls import path
from .views import ReceiptListView, CreateReceiptView, CreateItemView, DeleteReceiptView, DetailReceiptView, Title

app_name = 'receipt'

urlpatterns = [
    path('', Title),
    path('home/', ReceiptListView.as_view(), name='home'),
    path('forms/', CreateReceiptView.as_view(), name='receipt_form'),
    path('item_form/', CreateItemView.as_view(), name='item_form'),
    path('delete/<int:pk>/', DeleteReceiptView.as_view(), name='delete'),
    path('detail/<int:pk>/', DetailReceiptView.as_view(), name='detail')
]