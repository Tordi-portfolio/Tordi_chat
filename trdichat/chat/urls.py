from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('home', views.home, name='home'),
    path('guild', views.guild, name='guild'),
    path('join', views.join, name='join'),
    path('login', views.login, name='login'),
    path('sign_out', views.sign_out, name='sign_out'),

    # ... other urlpatterns ...
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
