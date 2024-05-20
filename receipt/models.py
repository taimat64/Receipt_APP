from django.db import models

class Receipt(models.Model):
    shop_name = models.CharField(max_length=20 ,blank=False)
    date_time = models.DateField()
    item_list = models.JSONField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)  # 合計金額

    def __str__(self):
        return f"{self.shop_name} - {self.date_time}"


class Item(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='items')  # レシートとの関連付け
    product_name = models.CharField(max_length=100)  # 商品名
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 価格
    quantity = models.PositiveIntegerField()  # 数量
    deadline = models.DateField(blank=True, null=True) #賞味・消費期限

    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product_name} - {self.price}"

