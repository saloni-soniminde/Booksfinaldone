from django.shortcuts import render
from . models import Books
# Create your views here.
def index(request):
    return render(request,'temp.html')
    #return render(request, 'rango/index.html', context)

def store(request):
    count=Books.objects.all().count()
    context={
        'count':count
    }
    return render(request,'hi.html',context)