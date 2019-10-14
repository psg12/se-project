from django import forms

from .models import balance,history


class add_money(forms.ModelForm):
    class Meta:
        model=balance
        fields=["balance","remark"]
class sendform(forms.ModelForm):
    someone=forms.CharField(max_length=255)
    class Meta:
        model=history
        fields=["someone","amount","remark"]