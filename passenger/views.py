from django.shortcuts import render
from .models import Passenger

# Create your views here.
def home(request):
    context = {
         'status':'Sorry,Working on the project'

    }
    return render(request,'index.html',context)


def dashboard(request):
    return render(request,'dashboard1.html')


def profile(request):
    return render(request,'user1.html')