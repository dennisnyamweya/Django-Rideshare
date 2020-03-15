from django.shortcuts import render
from .models import Driver

# Create your views here.
def home(request):
    context = {
         'status':'Sorry,Working on the project'

    }
    return render(request,'index.html',context)
