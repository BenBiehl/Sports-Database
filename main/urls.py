from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("login_page/", views.login_page, name="login_page"),
    path("signup_page/", views.signup_page, name="signup_page"),
    path("user/<str:user_name>/", views.user_page, name="user_page"),
    path("logout/", views.logout, name="logout"),
    path("baseball/", views.baseball_page, name="baseball_page"),
    path("basketball/", views.basketball_page, name="basketball_page"),
    path("soccer/", views.soccer_page, name="soccer_page"),
    path("football/", views.football_page, name="football_page")
]