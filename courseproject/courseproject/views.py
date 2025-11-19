from django.shortcuts import render,redirect
from . import models


def register (request):
    if request.method ==  "GET":
        return render(request,"registration.html")
    else:
        fullname=request.POST.get("fullname")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        role = "student"
        res=models.mstuser(fullname=fullname,gender=gender,mobile=mobile,address=address,email=email,pwd=pwd,role=role)
        res.save()
        return render(request,"registration.html")
    
def home (request):
    return render (request,"index.html")

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        pwd=request.POST.get("pwd")
        result=models.mstuser.objects.filter(email=email,pwd=pwd)
        if len(result)>0:
            print("login success")
            role = result[0].role
            print("role : ",role)
            #for create new session..........................................................
             
            request.session["email"]=email
            request.session["role"]=role
            #................................................................................
            if role =="student":
                return redirect("/studenthome/")
            elif role=="admin":
                return redirect("/adminhome/")
        else:
            print("Invalid Email id or Password")
        return render(request,"login.html")
    else:
        return render(request,"login.html")

def studenthome(request):
    return render(request,"studenthome.html")

def adminhome(request):
    return render(request,"adminhome.html")