"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "main"

urlpatterns = [
    path("", views.welcome, name='welcome'), 
    path("specialist/",views.prediction, name="specialist"),
    path("public/",views.prediction_public, name="public"),
    path("signin/", views.registerPage , name="signin"),
    path("login/",views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("profile/",views.profile, name="profile"),
    path("history/",views.view_history, name="history"),
    path('delete_prediction/<int:prediction_id>/', views.delete_prediction, name='delete_prediction'),
    
]
