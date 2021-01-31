from django.shortcuts import render, HttpResponse, redirect

from .models import userInfo,User,genre,book,cart,order

from .forms import userForm,Login_form

# Create your views here.
def home(request):    
    gen=genre.objects.all()
    boo=book.objects.all()
    d={'gen':gen,'boo':boo}
    return render(request,'home.html',d)

def get_by_genre(request,id):
    gen=genre.objects.all()
    boo=book.objects.filter(genre=id)
    d={'gen':gen,'boo':boo}
    return render(request,'home.html',d)


def search_product(request):
    gen=genre.objects.all()
    boo=book.objects.all()

    if request.method=='POST':
        name=request.POST.get('srch')
        boo=book.objects.filter(name__contains=name)
        d={'gen':gen,'boo':boo}
        return render(request,'search.html',d)
    
    else:
        d={'gen':gen,'boo':boo}
        return render(request,'search.html',d)

def addUser(request):
    cl=genre.objects.all()
    if request.method=='POST':
        f= userForm(request.POST)
        f.save()
        d={'cl':cl}
        return render(request,'login.html',d)

    else:
        f=userForm
        d={'cl':cl,'form':f}
        return render(request,'form.html',d)

from django.contrib.auth import login as dj_login,logout as dj_logout,authenticate
def login_view(request):
    cl=genre.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            dj_login(request,user)
            request.session['uid'] = user.id
            
            gen=genre.objects.all()
            boo=book.objects.all()
            d={'gen':gen,'boo':boo}
            return render(request,'home.html',d)
            #return redirect('/')
        else:
            return HttpResponse("InValid userName or password")
    else:
        f=Login_form
        d={'cl':cl,'form':f}
        return render(request,'login.html',d)

def logout_view(request):
    dj_logout(request)
    return redirect('/')


from django.contrib.auth.models import User
from .models import cart,order

def add_cart(request,id):
    b = book.objects.get(id = id)
    uid = request.session.get('uid')
    
    u = User.objects.get(id = uid)
    #create instance of model
    crt = cart()
    crt.user = u
    crt.book = b
    crt.save()
    return redirect('/')

def cart_list(request):
    uid = request.session.get('uid')
    if request.method == 'POST':

        my_ord = order()
        my_ord.total_bill =  request.POST.get('bill')   
        my_ord.user = User.objects.get(id = uid)
        my_ord.save()
        # crlist=Cart.objects.filter(user=uid)
        # for c in crlist:
        #     c.delete()
        cart_items =  request.POST.get('cart_items')   
        return redirect('/')

    else:
        cl = genre.objects.all()
        crlist = cart.objects.filter(user = uid)

        totalBill = 0
        for i in crlist:
            totalBill += i.book.price

    d = {'cl':cl, 'totalBill':totalBill, 'crlist':crlist}
    return render(request,'cartlist.html',d)

def my_order(request):
    cl=genre.objects.all()
    uid=request.session.get('uid')
    orlist=order.objects.filter(user=uid)
    d={'cl':cl,'orlist':orlist}
    return render(request,'orderlist.html',d)


