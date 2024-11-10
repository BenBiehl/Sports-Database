from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.landing_page, name="landing_page"),
    path("login_page/", views.login_page, name="login_page"),
    path("signup_page/", views.signup_page, name="signup_page"),
    path("user/<str:user_name>/", views.user_page, name="user_page"),
    path("logout/", views.logout, name="logout"),
    path("<str:sport>/", views.sports_page, name ="sports_page"),
    path("<str:sport>/add_athlete/", views.add_athlete, name="add_athlete"),
]