from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View
from .models import Receipt, Item
from django.views.generic.edit import FormView
from .forms import ReceiptForm, ItemForm
from django.urls import reverse_lazy
from django import forms



#タイトル画面
def Title(request):
    return render(request, 'receipt/title.html')
    
#一覧画面
class ReceiptListView(ListView):
    template_name = 'receipt/home.html'
    model = Receipt  # この行を追加
    


#作成画面
class CreateReceiptView(CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipt/forms.html'
    success_url = reverse_lazy('receipt:item_form')

    #ItemFormの受け渡し
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_form'] = ItemForm()
        return context

#Form複製時に必要なデータ    
FORM_NUM = 1
FORM_VALUES = {}


class CreateItemView(FormView):
    template_name = 'receipt/item_form.html'
    success_url = reverse_lazy('receipt:item_form')
    ItemFormset = forms.formset_factory(
        form=ItemForm,
        extra=1,
        max_num=50,
    )
    form_class = ItemFormset

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if FORM_VALUES and 'btn_add' in FORM_VALUES:
            kwargs['data'] = FORM_VALUES
        return kwargs
    
    def post(self, request, *args, **kwargs):
        global FORM_NUM
        global FORM_VALUES

        if 'btn_add' in request.POST:
            FORM_NUM += 1
            FORM_VALUES = request.POST.copy()
            FORM_VALUES['form-TOTAL_FORMS'] = FORM_NUM
# Subtract
        if 'btn_sub' in request.POST:
            if FORM_NUM > 1:
                FORM_NUM -= 1
            FORM_VALUES = request.POST.copy()
            FORM_VALUES['form-TOTAL_FORMS'] = FORM_NUM

        if 'btn_submit' in request.POST:
            self.success_url = reverse_lazy('receipt:home')
            FORM_VALUES = {}

        return super().post(request, args, kwargs)
    
    def form_valid(self, form):
        if 'btn_submit' in self.request.POST:
            data = form.cleaned_data

            for item_parameter in data:
                if item_parameter:
                    item = Item(**item_parameter)
                    item.save()
        return super().form_valid(form)


class DeleteReceiptView(DeleteView):
    model = Receipt
    success_url = reverse_lazy('receipt:home')
    template_name = 'receipt/receipt_delete.html'

class DetailReceiptView(DetailView):
    template_name = 'receipt/detail.html'
    model = Receipt  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # ビューが処理する特定の Receipt インスタンスを取得
        receipt = self.get_object()
        receipt_id = receipt.pk
        
        # receipt_id を使用して関連する Item インスタンスを取得
        items = Item.objects.filter(receipt=receipt_id)

        context['id'] = receipt_id
        context['item'] = items  # コンテキストキーを 'item' から 'items' に変更

        return context
    

class KakeiboView(View):
    def get(self, request, *args, **kwargs):
        
        return 
        