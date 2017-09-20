from django import forms

class Survey(forms.Form):
    name = forms.CharField(label="Name", max_length=255)
    bday = forms.DateField(label="Birthday")
    email = forms.EmailField(label="Email", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    # class Meta:
    #     model = user
