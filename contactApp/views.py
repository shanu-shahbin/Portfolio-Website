from django.shortcuts import render
from .forms import ContactForm
from .models import Contact_form, Connections

def Contact(request):
    connections = Connections.objects.first()
    email = connections.email
    phone_number = connections.phone_number
    instagram_link = connections.instagram
    twitter_link = connections.twitter
    linkedin_link = connections.linkedin
    github_link = connections.github

    success_message = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create and save a new Contact_form object
            contact = Contact_form.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
                organization_name=form.cleaned_data['organization_name'],
                services_needed=form.cleaned_data['services_needed']
            )
            success_message = "Your message has been sent successfully!"
            form = ContactForm()  # Clear the form for new input
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'success_message': success_message,
        'email': email,
        'phone_number': phone_number,
        'instagram_link': instagram_link,
        'twitter_link': twitter_link,
        'linkedin_link': linkedin_link,
        'github_link': github_link,
    })
