from django import forms


class Contact_form(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'first_name'}))
    last_name = forms.CharField(label="Last name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'last_name'}))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'name':'email'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control', 'name':'message'}))
    