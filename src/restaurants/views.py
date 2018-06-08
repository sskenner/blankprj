import random
from django.http import HttpResponse
from django.shortcuts import render

# funcation based view
def home(request):
    num = None
    some_list = [
        random.randint(0, 1000000000),
        random.randint(0, 1000000000),
        random.randint(0, 1000000000)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0, 1000000000)
    context = {
        "num": num,
        "some_list": some_list
    }
    return render(request, "home.html", context)

def about(request):
    context = {
    }
    return render(request, "about.html", context)

def contact(request):
    context = {
    }
    return render(request, "contact.html", context)