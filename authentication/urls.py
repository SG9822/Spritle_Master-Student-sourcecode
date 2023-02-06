from django.urls import path
from. views import MasterLogin, home, register, StudentLogin, TaskList, teacherhome, studenthome, TaskCreate, AnswerCreate, AnswerList,signout, pythonans,inputs
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('teacherhome/', teacherhome, name='teacherhome'),
    path('studenthome/', studenthome, name='studenthome'),
    path('login/', MasterLogin.as_view(), name='login'),
    path('studentlogin/', StudentLogin.as_view(), name='studentlogin'),
    path('signout/',signout,name='signout'),
    path('register/', register, name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('task/', TaskList.as_view(), name="tasklist"),
    path('taskcreate/', TaskCreate.as_view(), name="taskcreate"),
    path('answer/', AnswerList.as_view(), name="anslist"),
    path('anscreate/', AnswerCreate.as_view(), name="anscreate"), 
    path('pythonans', pythonans, name="pythonans"),
    path('input/', inputs, name='input'),
]