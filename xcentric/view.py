from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login ,authenticate

User = get_user_model()
def fun(request):
    if(request.method=="POST"):
         name=request.POST["name"]
         email=request.POST["email"]
         password=request.POST["password"]
         re_password=request.POST["re_password"]
         user = User.objects.create_user(name, email, password)
         user.save()

         login(request, user)
         print(name)
         return render(request, "main_home.html",{'loggedin':True}) 
    return render(request, "main_home.html",{'loggedin':False})

def log(request):
    if(request.method=="POST"):
        name=request.POST["name"]
        password=request.POST["password"]
        user=authenticate(request,username=name,password=password)
        if(user is not None):
            login(request, user)
            return render(request, "main_home.html",{'loggedin':True}) 
    return render(request, "main_home.html",{'loggedin':False})


def mind(request):
    return render(request, "mind_home.html") 

def fit(request):
    return render(request, "fitness_home.html")        

def plan(request):
    return render(request, "planner_home.html")

def diary(request):
    return render(request, "diary_home.html")  

def riddle(request):
    return render(request, "riddle_home.html")        

def fitgain(request):
     return render(request, "fitness_gain.html")

def fitloss(request):
     return render(request, "fitness_loss.html")

def todo(request):
     return render(request, "planner_todo.html")

def calender(request):
     return render(request, "planner_calendar.html")   

def entry(request):
     return render(request, "diary_page.html")        

def riddle1(request):
    return render(request, "riddle_pg1.html")

def riddle2(request):
    return render(request, "riddle_pg2.html")

def riddle3(request):
    return render(request, "riddle_pg3.html")    