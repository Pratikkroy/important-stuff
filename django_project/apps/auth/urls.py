from django.urls import path, include
from apps.auth.views import Auth,Login,Register,Logout,Token,Profile
from apps.auth.views import Credentials
from src.constants import UpdateCredentialsType

urlpatterns = [
    path('',Auth.as_view(), name="auth"),
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', Logout.as_view(), name="logout"),
    path('token/refresh/', Token.as_view(), name="token"),
    path('profile/', Profile.as_view(), name="profile"),
    path('profile/cr/', Credentials.as_view(), name="update_credentials"),
]