from django.shortcuts import render

# Create your views here.
def skill(request):
    context = {'skilla': 'active'}
    return render(request, 'edu_t/skill.html', context)