from django.urls import path
from users.views import login_view, register_view, logout_views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_views, name='logout'),
]