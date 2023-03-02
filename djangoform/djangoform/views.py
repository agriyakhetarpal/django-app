from django.http import HttpResponse
from django.shortcuts import render, redirect
from djangoform.forms import ContactForm

# display and process the form after validating the data
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

 # view to display the success page
def success(request):
    return render(request, 'success.html')
