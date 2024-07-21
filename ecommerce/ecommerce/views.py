from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from apps.models import UserCreateForm 
from apps.models import Category,Product,Contact_us,Order,Brand
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
#cart section
@login_required(login_url="/accounts/login/")
def cart_add(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="/accounts/login/")

def item_clear(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/accounts/login/")

def item_increment(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/accounts/login/")

def item_decrement(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/accounts/login/")

def cart_clear(request):
    cart=Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request,'cart/cart_detail.html')


from apps.models import Category,Sub_Category,Product

def Master(request):
    return render(request,'master.html')
def Index(request):
    category=Category.objects.all()
    brand=Brand.objects.all()
    product=Product.objects.all()
    brandId=request.GET.get('brand')
    categoryId=request.GET.get('category')

    if categoryId:
        product=Product.objects.filter(sub_category=categoryId).order_by('-id')
    elif brandId:
        product=Product.objects.filter(brand=brandId).order_by('-id')    
    else:
        product=Product.objects.all()    
    context={
        'category':category,
        'product':product,
        'brand':brand,
    }
    return render(request,'index.html',context)
def SignUp(request):
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            new_user=authenticate(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],

            )
            login(request,new_user)
            return  redirect('index')
    else:
        form=UserCreateForm
    context={
        'form':form,
    }    
    return render(request,'registration/signup.html',context)
#def Login(request):
    
    return render(request,'registration/login.html')


def Contact_Page(request):
    if request.method=='POST':
        contact = Contact_us(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        contact.save()

    return render(request,'contact.html')

def Checkout(request):
    if request.method=="POST":
        number=request.POST.get('number')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        print(address,number,pincode)
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        for i in cart:
            a=(int(cart[i]['price']))
            b=(int(cart[i]['quantity']))
            total=a*b
            order=Order(
                user=user,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                address=address,
                phone=number,
                pincode=pincode,
                total=total,
            )
            order.save()
            request.session['cart']={}
            return redirect('index')
    return HttpResponse("This is checkout page !")


def Your_Order(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(pk=uid)
    order=Order.objects.filter(user=user)
    
    context={
        'order':order,
    }
    return render(request,"order.html",context)
def Product_Page(request):
    
    category=Category.objects.all()
    brand=Brand.objects.all()
    
    brandId=request.GET.get('brand')
    categoryId=request.GET.get('category')

    if categoryId:
        product=Product.objects.filter(sub_category=categoryId).order_by('-id')
    elif brandId:
        product=Product.objects.filter(brand=brandId).order_by('-id')    
    else:
        product=Product.objects.all() 
    context={
        'category':category,
        'brend':brand,
        'product':product,
        
    }
    return render(request,'product.html',context)
def Product_Detail(request,id):
    product=Product.objects.filter(id=id).first()
    context={
        'product':product,
    }
    return render(request,'product_detail.html',context)
def Search(request):
    query=request.GET['query']
    product=Product.objects.filter(name__icontains=query)
    context={
        'product':product,
    }
    return render(request,'search.html',context)