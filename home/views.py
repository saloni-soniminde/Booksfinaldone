from django.shortcuts import render
from . models import Books
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'temp.html')

def store(request):
    count=Books.objects.all().count()
    context={
        'count':count,

    }
    request.session['location']="unknown"
    if request.user.is_authenticated:
        request.session['location'] = "Earth"
    return render(request,'base.html',context)
