
from django.contrib import admin
from django.urls import path , include
from accounts.views import SignupView

urlpatterns = [
    
    path("create",SignupView.as_view(),name="signup"),
]
