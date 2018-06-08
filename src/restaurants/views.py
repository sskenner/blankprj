import random
from django.http import HttpResponse
from django.shortcuts import render

# funcation based view
# def home(request):
#     html_var = 'f strings'
#     html_ = f"""<!DOCTYPE html>
#     <html lang=en>
#     <head>
#     </head>
#     <body>
#     <h1>sup world!</h1>
#     <p>this is {html_var} coming through</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)
#     # return render(request, "home.html", {})

def home(request):
    num = random.randint(0, 1000000000)
    return render(request, "base.html", {"html_var": True, "num": num})