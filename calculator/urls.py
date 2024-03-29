from django.urls import path
from .views import  calculate_form, calculate_result, login_from, login
urlpatterns = [
    path("",login_from ),
    path("login/", login),
    path("calculate_form/", calculate_form, name = "calculator"),
    path("result/", calculate_result,name= "result" ),
]
