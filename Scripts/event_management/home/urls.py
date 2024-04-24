from django.urls import path , include
from .views import authView , home
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from .views import *


app_name = 'home'


urlpatterns = [
    path("", home , name ="home"),
    path('information',information, name='information'),
    path("delete_information/<int:id>/", delete_information, name="delete_information"),
    path("update_information/<int:id>/", update_information, name="update_information"),
    path("signup/", authView , name="signup"),
    path("login/", authView , name="login"),
    path("accounts/", include("django.contrib.auth.urls")),

] + static(settings.STATIC_URL)

