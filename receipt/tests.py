from django.test import TestCase
from .models import Item
from django.db import models


class Mymodel(models.Model):
    test_model = models.JSONField()

    def __str__(self):
        return self.test_model
    
def test(self):
    for item in Item.objects.all():
        obj = Mymodel(test_model=item)
    obj.save()

    print(obj)

print(test)

        
