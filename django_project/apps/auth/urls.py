from django.urls import path, include
from apps.auth.views import Auth,Login

urlpatterns = [
    path('',Auth.as_view(), name="auth"),
    path('login/', Login.as_view(), name="login")
]