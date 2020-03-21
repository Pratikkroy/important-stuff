from django.urls import path, include
from apps.auth.views import Auth,Login,Register,Logout, Token

urlpatterns = [
    path('',Auth.as_view(), name="auth"),
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', Logout.as_view(), name="logout"),
    path('token/refresh/', Token.as_view(), name="token"),
]