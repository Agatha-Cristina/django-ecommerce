from django import forms
class ContractForms(forms.Forms):
    fullname= forms.CharField()
    email = forms.EmailField()
    content = forms.CharField()