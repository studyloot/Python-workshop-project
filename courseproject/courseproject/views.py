from django.shortcuts import render,redirect
from . import models
def register(request):
    if request.method=="GET":
        return render(request,"registration.html")
    else: 
        fullname=request.POST.get("fullname")
        gender=request.POST.get("gender")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        role="student"
        res=models.mstuser(fullname=fullname,gender=gender,mobile=mobile,address=address,emailid=emailid,pwd=pwd,role=role)
        res.save()
        return render(request,"registration.html")
    
def home(request):
    return render(request,"index.html")
    def login(request):
        return render(request,"login.html")

def login(request):
    if request.method=="POST":
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        result=models.mstuser.objects.filter(emailid=emailid,pwd=pwd)
        if len(result)>0:
            print("login success")
            #for fetch role value from database table
            role=result[0].role
            print("role- ",role)
            if role =="student":
                return redirect("/studenthome")
        else:
            print("Invalid Email id or Password")
        return render(request,"login.html")
    else:
        return render(request,"login.html")
    

def studenthome(request):
    return render (request,"studenthome.html")