from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.  

def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{ 'Employees':emps}) 

def add_emp(request):
    if request.method=="POST":
        print("data is coming")

        #validation

        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department") 

        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        #save the object
        e.save() 
        #prepare message


        return redirect("/emp/home/") 
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,e_id_gpk):
    print(e_id_gpk) 
    emp=Emp.objects.get(id=e_id_gpk) 
    emp.delete()
    return redirect('/emp/home/') 

def update_emp(request,e_id_gpk):
    print(e_id_gpk)
    emp=Emp.objects.get(id=e_id_gpk) 
    return render(request,"emp/update_emp.html",{'Employee': emp})  

def do_update_emp(request,e_id_gpk):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department") 

        #create model object and set the data
        e=Emp.objects.get(id=e_id_gpk) 
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        #save the object
        e.save() 
        #prepare message

    return redirect("/emp/home/")

     


