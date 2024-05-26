from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label="First Name", required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    num2=forms.CharField(label="Middle Name", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    num3=forms.CharField(label="Last Name", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email=forms.EmailField(label="Email Address", required=True, widget=forms.TextInput(attrs={'class':"form-control"}))