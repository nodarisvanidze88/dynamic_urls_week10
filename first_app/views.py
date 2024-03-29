from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
items = ["Apple", "Banana", "Orange", "Grapes"]
def index(request):
    new_items = "<br>".join(items)
    return HttpResponse(f"Items: <br>{new_items}")

def show_item(request,id):
    try:
        return HttpResponse(f"Selected: {items[id+1]}")
    except:
        return HttpResponse("Wrong ID")