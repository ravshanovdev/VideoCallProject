from django.urls import path
from .views import register, login_view, dashboard, videocall, index, logout_view, join_meeting

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('meeting/', videocall, name='meeting'),
    path('logout/', logout_view, name='logout'),
    path('join_meeting/', join_meeting, name='join_meeting')



]

