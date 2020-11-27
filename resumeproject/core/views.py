from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'homea': 'active'}
    return render(request, 'core_t/home.html', context)


def contact(request):
    context = {'contacta': 'active'}
    return render(request, 'core_t/contact.html', context)