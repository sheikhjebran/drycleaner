from django.urls import path

from . import views

urlpatterns = [
    # webpage URL
    path('', views.login, name="login"),
    path('authenticate', views.get_authenticate, name="get_authenticate"),
]