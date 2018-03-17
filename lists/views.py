from django.shortcuts import render
# Create your views here.


def home_page(request):
    """View of Homepage."""
    return render(request, 'home.html')
