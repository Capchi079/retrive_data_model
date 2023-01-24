from django.shortcuts import render
from app.models import *
# Create your views here.
def Topic_details(request):
    t=Topic.objects.all()
    d={'topic':t}
    return render(request,'Topic_details.html',d)


def Webpage_details(request):
    w=Webpage.objects.all()
    d={'webpage':w}
    return render(request,'Webpage_details.html',d)
