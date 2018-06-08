from django.http import HttpResponse
from django.shortcuts import render

# funcation based view
def home(request):
    html_var = 'f strings'
    html_ = f"""<!DOCTYPE html>
    <html lang=en>
    <head>
    </head>
    <body>
    <h1>sup world!</h1>
    <p>this is {html_var} coming through</p>
    </body>
    </html>
    """
    return HttpResponse(html_)
    # return render(request, "home.html", {})
