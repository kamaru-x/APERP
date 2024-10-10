from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    context = {
        'main' : 'dashboard'
    }
    return render(request,'dashboard/index.html',context)