from django.shortcuts import render

# Create your views here.
def services(request):
    context = {'servicesa': 'active'}
    return render(request, 'serv_t/services.html', context)