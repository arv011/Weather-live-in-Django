from django import forms

class weatherform(forms.Form):
    city = forms.CharField(max_length=20, required=False)
    pincode = forms.CharField(max_length=40, required=False)
