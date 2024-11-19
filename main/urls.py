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
    path("<str:sport>/athlete/<str:athlete_id>/", views.athlete_page, name="athlete_page"),
    path("<str:sport>/athlete/<str:athlete_id>/edit", views.edit_athlete, name="edit_athlete"),
    path("athlete/search/", views.search_page, name="search_page"),
    path("<str:sport>/athlete/<str:athlete_id>/favorite/<str:user_name>/", views.favorite_athlete, name="favorite_athlete"),
    path("<str:sport>/athlete/<str:athlete_id>/delete", views.delete_athlete, name="delete_athlete"),
    path("secrets/easter_egg/", views.easter_egg, name="easter_egg")
]