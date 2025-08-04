from django.urls import path
from .views import user_login, logout_user, home, signup

urlpatterns = [
    path('', user_login, name='login'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
]
