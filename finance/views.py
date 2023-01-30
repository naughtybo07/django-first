from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import bank,supplier,customer,approve_invoice,request_invoice,deny_invoice,view_invoice,upload_invoice
from .forms import bankforms,supplierforms,customerforms
from django.contrib.auth import logout 
from django.contrib import messages

# Create your views here.

def bank_forms(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        emp_code=request.POST.get('emp_code')
        phnum=request.POST.get('phnum')
        email=request.POST.get('email')
        joining_date=request.POST.get('joining_date')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
    
        if password1==password2:
            if bank.objects.filter(name=name).exists():
                return render(request,'bank_reg.html',{'Incorrect':' Invalid login'})
                print('username taken')
            elif bank.objects.filter(email=email).exists():   
                print('Email taken') 
            else:
                user= bank.objects.create(name=name,password1=password1,email=email,address=address,emp_code=emp_code,phnum=phnum,joining_date=joining_date)
                user.save()
                print('user created successfully')
                return render(request,'home.html')
        else:
            return render(request,'bank_reg.html',{'Incorrect':'Password Is Not Matching'})

    return render(request,'bank_reg.html')

def supplier_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        emp_code=request.POST.get('emp_code')
        phnum=request.POST.get('phnum')
        email=request.POST.get('email')
        Credit_Ac_num=request.POST.get('Credit_Ac_num')
        credit_info=request.POST.get('credit_info')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        if password1==password2:
            if supplier.objects.filter(name=name).exists():
                print('username taken')
            elif supplier.objects.filter(email=email).exists():   
                print('Email taken') 
            else:
                user= supplier.objects.create(name=name,password1=password1,email=email,address=address,emp_code=emp_code,phnum=phnum,Credit_Ac_num=Credit_Ac_num,credit_info=credit_info)
                user.save()
                print('user created successfully')
                return render(request,'home.html')
        else:
            return render(request,'suplier_reg.html',{"Incorrect":"Password Is Not Matching"})

    return render(request,'suplier_reg.html')

def customer_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phnum=request.POST.get('phnum')
        email=request.POST.get('email')
        loan_Ac_num=request.POST.get('loan_Ac_num')
        loan_info=request.POST.get('loan_info')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        if password1==password2:
            if customer.objects.filter(name=name).exists():
                print('username taken')
            elif customer.objects.filter(email=email).exists():   
                print('Email taken') 
            else:
                user= customer.objects.create(name=name,password1=password1,email=email,address=address,phnum=phnum,loan_Ac_num=loan_Ac_num,loan_info=loan_info)
                user.save()
                print('user created successfully')
                return render(request,'home.html')
        else:
            return render(request,'customer_reg.html',{"Incorrect":"Password Is Not Matching"})

    return render(request,'customer_reg.html')
    
def bank_login(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('password1')
        try:
            name1=bank.objects.get(name=a)
            if c== name1.password1:
                request.session['username'] = a
                return render(request,'bank_main.html',{'bankname':a})
                
        except Exception as e:
            
            return render(request,'bank_login.html',{'message':'No user found'})
            
 
    return render(request,'bank_login.html')

def supplier_login(request):
    if request.method=='POST':
        x = request.POST.get('name')
        y = request.POST.get('email')
        z = request.POST.get('password1')
        try:
            name2=supplier.objects.get(name=x)
            if z == name2.password1: 
                return render(request,'supplier_main.html')
        except Exception as er:
            print(er)
            return render(request,'supplier_login.html',{'message':'No user found'})
        
    return render(request,'supplier_login.html')
        
def customer_login(request):
    if request.method=='POST':
        na = request.POST.get('name')
        b = request.POST.get('email')
        pa = request.POST.get('password1')
        try:
            name3=customer.objects.get(name=na)
            if pa == name3.password1 :
                return render(request,'customer_main.html')
        except Exception as error:
            return render(request,'customer_login.html',{'message':'No user found'})
        
    return render(request,'customer_login.html')

def req_invoice(request):
    requested = upload_invoice.objects.all()
    if request.method== 'POST':
        sup1_code = request.POST.get('sup_code')
        num1= request.POST.get('in_num')
        date1= request.POST.get('in_date')
        amount1=request.POST.get('in_amount')
        currency1= request.POST.get('currency')
        
        user = request_invoice.objects.create(sup_code=sup1_code,in_num=num1,in_amount=amount1,currency=currency1)
        user.save()
        del_up= upload_invoice.objects.get(in_num=num1)
        del_up.delete()
        
        return render(request,'request.html')
    return render(request,'R_invoice.html',{'request1':requested})

def app_invoice(request):
    approveed= upload_invoice.objects.all()
    if request.method== 'POST':
        sup2_code = request.POST.get('sup_code')
        num2= request.POST.get('in_num')
        date2 = request.POST.get('in_date')
        amount2= request.POST.get('in_amount')
        currency2=request.POST.get('currency')
        
        
        user1 = view_invoice.objects.create(sup_code=sup2_code,in_num=num2,in_amount=amount2,currency=currency2)
        user1.save()
        if num2=='request_invoice':
            request_invoice.remove()    

    return render(request,'A_invoice.html',)
    

def approveinvoice(request):
    a= request_invoice.objects.all()
    if "approve" in request.POST:
        ccode=request.POST.get('sup_code')
        cnum = request.POST.get('in_num')
        camount = request.POST.get('in_amount')
        cdate = request.POST.get('in_date')
        ccurrency = request.POST.get('currency')
        approval = approve_invoice.objects.create(sup_code=ccode,in_num=cnum,in_amount=camount,currency=ccurrency)
        approval.save()
        deletes = request_invoice.objects.get(in_num=cnum)
        deletes.delete()
        print(deletes)

        return render(request,'approve.html')
    if 'deny' in request.POST:
        dcode=request.POST.get('sup_code')
        dnum = request.POST.get('in_num')
        damount = request.POST.get('in_amount')
        ddate = request.POST.get('in_date')
        dcurrency = request.POST.get('currency')
        approve = deny_invoice.objects.create(sup_code=dcode,in_num=dnum,in_amount=damount,currency=dcurrency)
        approve.save()
        delete1 = request_invoice.objects.get(in_num=dnum)
        delete1.delete()

        print('delete')
        return render(request,'deny.html')  
    
    return render (request,'A_invoice.html',{'data':a})
   
def A_viewinvoice(request):
    user2 = request.session['username']
    view=  approve_invoice.objects.all()
    if request.method=='POST':
        name= request.POST.get('name')
        phnum=request.POST.get('phnum')
        client_code= request.POST.get('client_code')
        loan_amount= request.POST.get('loan_amount')
        view1= view_invoice.objects.create(name=name,phnum=phnum,client_code=client_code,loan_amount=loan_amount)
        view1.save()
        
    return render(request,'A_viewinvoice.html',{'data1':view,'name_user':user2})

def D_viewinvoice(request):
    user2 = request.session['username']
    deny=  deny_invoice.objects.all()
    if request.method=='POST':
        name= request.POST.get('name')
        phnum=request.POST.get('phnum')
        client_code= request.POST.get('client_code')
        loan_amount= request.POST.get('loan_amount')
        deny1= view_invoice.objects.create(name=name,phnum=phnum,client_code=client_code,loan_amount=loan_amount)
        deny1.save()
        
        
    return render(request,'D_viewinvoice.html',{'deny2':deny,'users':user2})

def our_supplier(request):
    
    our = supplier.objects.all()
    for i in our:
        print(i.name)
    return render(request,'our_suppliers.html',{'our2': our})

def our_customer(request):
    cus = customer.objects.all()
    return render(request,'our_customers.html',{'cus2':cus})

def up_invoice(request):
    if request.method == 'POST':
        su_code=request.POST.get('sup_code')
        num = request.POST.get('in_num')
        date = request.POST.get('in_date')
        amount = request.POST.get('in_amount')
        currency= request.POST.get("currency")
        
        if upload_invoice.objects.filter(in_num=num).exists():
            return render(request,'uploadinvoice.html',{'mgs1':'INVOICE NUMBER IS ALREADY TAKEN'})
        else:
            upload = upload_invoice.objects.create(sup_code=su_code,in_num=num,in_date=date,in_amount=amount,currency=currency)
            upload.save()
            return render(request,'uploadinvoice.html',{'mgs':'YOUR INVOICE HAS BEEN UPLOADED SUCCESS FULLY'})
        
    return render(request,"uploadinvoice.html")

def bankmain(request): 
    user1 = request.session['username']
    return render(request,'bank_main.html',{'bankname':user1})
    
def home(request):
    return render(request,'home.html')  

def suppliermain(request):
    return render(request,'supplier_main.html')

def customermain(request):
    return render(request,'customer_main.html')

def viewinvoice(request):
    return render(request,'viewinvoice.html')