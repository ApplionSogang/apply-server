from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns= [

    path('login/home/', login_home, name="login_home"),

    path('signup/email/', signup_email, name="signup_email"), 
    path('login/email/', email_login, name="email_login"), 


    path('login/kakao/', kakao_login, name="kakao_login"),
    path('kakao/login/callback/', kakao_login_callback, name="kakao_login_callback"), 
    path('kakao/submit/', submit_kakao, name="submit_kakao"),

    path('logout/', logout_view, name="logout"), 
    path('logout/with/kakao', logout_with_kakao, name="logout_with_kakao"),

    path('success/', success, name = "success"),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('send_email/', send_email, name='send_email'),
]
