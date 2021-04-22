from django.urls import path
from authentication.views import logout_user, login_user, register_user


urlpatterns = [
    path("logout", logout_user, name="logout"),
    path("login", login_user, name="login"),
    path("register", register_user, name="register")
]
