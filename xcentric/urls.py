"""xcentric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.fun,name="home"),
    path('login/',view.log,name="login"),
    path('mind/',view.mind,name="mindhome"),
    path('fit/',view.fit,name="fitnesshome"),
    path('planner/',view.plan,name="plannerhome"),
    path('diary/',view.diary,name="diaryhome"),
    path('riddle/',view.riddle,name="riddlehome"),
    path('fitgain/',view.fitgain,name="gain"),
    path('fitloss/',view.fitloss,name="loss"),
    path('todo/',view.todo,name="todolist"),
    path('calendar/',view.calender,name="calendar"),
    path('entry/',view.entry,name="diary"),
    path('riddle1/',view.riddle1,name="riddle1pg"),
    path('riddle2/',view.riddle2,name="riddle2pg"),
    path('riddle3/',view.riddle3,name="riddle3pg")


    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

