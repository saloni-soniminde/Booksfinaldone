from django.shortcuts import render
from . models import Books, BookOrder,  Cart
from django.shortcuts import render, redirect

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'temp.html')

def store(request):
    books=Books.objects.all()
    context={
        'books': books,
    }
    return render(request, 'base.html', context)

def book_details(request, book_id):

    context = {
        'book': Books.objects.get(pk=book_id),
    }
    return render(request, 'store/detail.html', context)

def add_to_cart(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Books.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user=request.user
                )
                cart.save()
            cart.add_to_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def remove_from_cart(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Books.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, active=True)
        orders = BookOrder.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in orders:
            total += (order.book.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('index')