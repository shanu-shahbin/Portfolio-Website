from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="What's your name?", max_length=100)
    email = forms.EmailField(label="What's your email?")
    message = forms.CharField(label="What's your message?", widget=forms.Textarea)
    organization_name = forms.CharField(label="What's the name of your organization?", max_length=100)
    services_needed = forms.CharField(label="What services are you looking for?", widget=forms.Textarea)
