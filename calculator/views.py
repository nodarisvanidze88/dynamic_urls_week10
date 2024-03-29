from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

def login_from(request):
    return HttpResponse("""
    <form action="login">
        <input type="text" name="user" placeholder="User">
        <input type="text" name="password" placeholder="Password">
        <input type="submit" value="Calculate">
    </form>
""")

def login(request):
    registered_user = "Admin"
    registered_pass = "123456"
    if "user" in request.GET and "password" in request.GET:
        user = request.GET["user"]
        password = request.GET["password"]
        if registered_user == user and registered_pass == password:
            return redirect("calculator")
        else:
            return HttpResponse("I do not know you")


def calculate_form(request):
    return HttpResponse("""
    <form action="/calculator/result/">
        <input type="number" name="num1" placeholder="Enter first num">
        <input type="number" name="num2" placeholder="Enter second num">
        <input type="submit" value="Calculate">
    </form>
""")


def calculate_result(request):
    if "num1" in request.GET and "num2" in request.GET:
        num1 = int(request.GET['num1'])
        num2 = int(request.GET['num2'])
        result = num1 * num2
        return HttpResponse(f"Your result is {result}")
    else:
        return HttpResponse(f"Wrong inputs")


