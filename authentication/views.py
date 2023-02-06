from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Tasks, Answer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout


# Create your views here.

def home(request):
    return render(request,'authentication/home.html')

def teacherhome(request):
    return render(request, 'authentication/teacherhome.html')

def studenthome(request):
    return render(request, 'authentication/student_home.html')

class MasterLogin(LoginView):
    template_name = 'authentication/login.html'
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('teacherhome')
    
class StudentLogin(LoginView):
    template_name = 'authentication/studentlogin.html'
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('studenthome')
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        if User.objects.filter(username=username):
            
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
          
            return redirect('home')
        
        if len(username)>15:
           
            return redirect('home')
        
        if pass1 != pass2:
          
            return redirect('home')
        
        if len(pass1) < 8:
        
           return redirect('home')  
       
        if not pass1.isalnum():
            return redirect('home')  
            
        
        if not username.isalnum():
            return redirect('home')
          
        
        
        myuser = User.objects.create_user(username=username, email=email, password=pass1, first_name = fname, last_name = lname)
        #myuser.first_name = fname
        #myuser.last_name = lname
        
        myuser.save()
        
        return redirect('home')
    
    
            
        
    return render(request,'authentication/register.html')

def signout(request):
    logout(request)
    return redirect('studentlogin')

class TaskList(ListView):
    model = Tasks
    context_object_name = "tasks"
    
    
class TaskCreate(CreateView):
    model = Tasks
    fields = ['question']
    success_url = reverse_lazy('tasklist')
    
class AnswerList(ListView):
    model = Answer
    context_object_name = "answers"
    
class AnswerCreate(CreateView):
    model = Answer
    fields = ['answer']
    success_url = reverse_lazy('anslist')
    
def inputs(request):    
    return render(request, 'authentication/input.html')    
    
def pythonans(request):
    value = request.GET["val"]
    req = value
    return render(request, 'authentication/python.html', {'Value':req})

    
        