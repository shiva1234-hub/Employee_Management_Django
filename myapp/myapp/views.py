
from django.http import HttpResponse 
from django.shortcuts import render
import datetime
def home(request):
    isActive = True
    if request.method=='POST':
        check=request.POST.get("check") 
        print(check) 

        if check is None: isActive=False
        else : isActive=True


    print("test function is called from view")
    date=datetime.datetime.now() 
    name="Toyozuki"
    list_of_programs=["Rajvanshi Festival","Bhosle Event","Bose Karya"]
    student={
        'student_name': "Ishaan Bose",
        'location': "Kolkata",
        'college': "ABC_Institute"
    }
    data={ 'date':date,
        'isActive':isActive,
          'name':name,
          'list_of_programs':list_of_programs,
          'student_data':student

         }
    #return HttpResponse("<h1>Hello, this is index page </h1>"+str(date))
    return render(request,"home.html",data)
    
def about(request):
    #return HttpResponse("<h1> This is about page </h1>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h1> This is services page </h1>")
    return render(request,"services.html",{})


    