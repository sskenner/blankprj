from django.http import HttpResponse
from django.shortcuts import render

# funcation based view
def home(request):
    return HttpResponse("hello")
    # return render(request, "home.html", {})
