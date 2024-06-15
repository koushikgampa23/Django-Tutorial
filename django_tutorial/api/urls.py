from django.urls import path
from .views import User, Login

urlpatterns = [
    path("login", Login.as_view()),
    path("signup", User.as_view()),
    # path("home", )
]
