from django import forms
from .models import bank,supplier,customer
class bankforms(forms.ModelForm):
    class Meta:
        model = bank
        fields = "__all__"
class supplierforms(forms.ModelForm):
    class Meta:
        model = supplier
        fields = "__all__"
class customerforms(forms.ModelForm):
    class Meta:
        model = customer
        fields = "__all__"