from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def package(request):
    return render(request, 'package.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def destination(request):
    return render(request, 'destination.html')

def guide(request):
    return render(request, 'guide.html')

def single(request):
    return render(request, 'Single.html')

def testmonial(request):
    return render(request, 'testimonial.html')                         


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

def success_view(request):
    pass