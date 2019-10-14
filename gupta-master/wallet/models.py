from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class balance(models.Model):
    WUser = models.ForeignKey(User,on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)
    remark=models.CharField(max_length=255)
    def __str__(self):
        return self.WUser.username
        
class history(models.Model):
    tosend=models.ForeignKey(User,related_name="to_person", on_delete=models.CASCADE)
    owner=models.ForeignKey(User,related_name="to_owner+", on_delete=models.CASCADE)
    remark=models.CharField(max_length=255)
    time=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField(default=0)
   
