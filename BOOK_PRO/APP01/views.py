from django.shortcuts import render,HttpResponse,redirect
from APP01 import models
from django.urls import reverse
# Create your views here.

def index(request):

    return  render(request,'index.html')

def book(request):
    all_objs=models.Book.objects.all()
    print(all_objs[0].pub_data)
    return  render(request,'book.html',{'all_objs':all_objs})

def add_book(request):
    if request.method=='GET':
        return render(request,'add_book.html')
    else:
        data=request.POST
        title=data.get('book_title')
        price = data.get('book_price')
        pub_date = data.get('book_pub_date')
        publish = data.get('book_publish')
        print(title,price,pub_date,publish)
        models.Book.objects.create(
            title=title,
            price=price,
            pub_data=pub_date,
            publish=publish
        )
        # return  HttpResponse('ok')
        return  redirect(reverse('books'))

def delete_book(request,book_id):
    models.Book.objects.filter(id=book_id).delete()
    return redirect(reverse('books'))

def update_book(request,book_id):
    if request.method=='GET':
        try:
            update_obj=models.Book.objects.get(id=book_id)
        except Exception:
            return HttpResponse('GGGGGGGGGGG')
        print(book_id)
        return render(request,'update_book.html',{'update_obj':update_obj,'book_id':book_id})
    else:
        data=request.POST
        title=data.get('book_title')
        price = data.get('book_price')
        pub_date = data.get('book_pub_date')
        publish = data.get('book_publish')
        print(title,price,pub_date,publish)
        models.Book.objects.filter(id=book_id).update(
            title=title,
            price=price,
            pub_data=pub_date,
            publish=publish
        )
        # return  HttpResponse('ok')
        return  redirect('books')
        # return  redirect(reverse('books'))
