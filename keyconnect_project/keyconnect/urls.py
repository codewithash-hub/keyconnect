from django.urls import path
from .views import user_login, logout_user

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
]
