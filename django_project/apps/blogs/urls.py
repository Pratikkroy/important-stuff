from django.urls import path, include
from apps.blogs import views

urlpatterns = [
    path('',views.Blogs.as_view(), name="blogs")
]