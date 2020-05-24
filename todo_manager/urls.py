"""todo_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('admin/', admin.site.urls),

    #auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    #everything to do with task
    path('', views.home, name='home'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('completed/', views.completed, name='completed'),
    path('createtask/', views.createtask, name='createtask'),
    path('viewtask/<int:todo_pk>', views.viewtask, name='viewtask'),
    path('todo/<int:todo_pk>/complete', views.completetask, name='completetask'),
    path('todo/<int:todo_pk>/delete', views.deletetask, name='deletetask'),
]
