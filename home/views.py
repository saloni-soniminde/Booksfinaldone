from django.shortcuts import render
from . models import Books
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'temp.html')

def store(request):
    books=Books.objects.all().count()
    context={
        'books':books,

    }

    return render(request,'base.html',context)
